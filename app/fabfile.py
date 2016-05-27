from fabric.api import env, run, sudo, local, runs_once, cd, prefix, parallel
# Uncomment this two lines  if you need debug mode
# import paramiko
# paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

# gce conf
GCE_PROJECT = 'newsai-1166'
GCE_ZONE = 'us-east1-c'
GCE_HOSTMATCH = 'newsai-context-api-3-.*'


def CONTEXT():
    """Preconf CONTEXT to do action 
    Deploy with `fab CONTEXT deploy`    
    """
    env.domain_name = "CONTEXT"
    gcloud()
    env.hosts = gcloud_hosts(GCE_PROJECT, GCE_ZONE, GCE_HOSTMATCH)


def gcloud_hosts(project, zone, match):
    """Retrieve from google sdk tool the hosts we want to deploy code
    Extracts all public ip addresses from hosts in project/zone 
    and name matching pattern (hosts in group should have groupname in hostname)
    """
    hosts = []
    data = {'project': project, 'zone': zone, 'match': match}
    gcloud = local(
        'gcloud --project "%(project)s" compute instances list --zone "%(zone)s" -r "%(match)s"' % data, capture=True)
    for line in gcloud.split('\n')[1:]:
        items = filter(lambda x: x, line.split(' '))
        hosts.append(items[-2])
    return hosts


def gcloud():
    """Defines google compute engine environment. Deploys will be done with 
    current user and current gcloud sdk auth.
    """
    env.user = local('whoami', capture=True)
    env.password = ''
    env.key_filename = '~/.ssh/google_compute_engine'
    env.env_file = "requirements.txt"


@parallel
def deploy():
    with cd("/var/apps/context"), prefix('source /var/apps/context/context/bin/activate'):
        with cd("/var/apps/context/api/app"):
            run('git pull origin master')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('echo yes | python manage.py collectstatic')
            run('supervisorctl reread')
            run('supervisorctl update')
            run('supervisorctl restart gunicorn')

# Source: https://gist.github.com/trilopin/8e305575f50bb0c6396f
