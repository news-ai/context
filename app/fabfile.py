# First we import the Fabric api
from fabric.api import *
from fabric.contrib.files import exists

# We can then specify host(s) and run the same commands across those systems
env.user = 'api'
env.key_filename = ['~/.ssh/id_rsa']
env.hosts = ['172.99.68.57']

@hosts(['172.99.68.57'])
def deploy():
    # Create a directory on a remote server, if it doesn't already exists
    if not exists('/home/api/context/api'):
        run('mkdir -p context/api')

    # Create a virtualenv, if it doesn't already exists
    if not exists('/home/api/context/context'):
        with cd('/home/api/context'):
            run('virtualenv context')

    # Activate the environment and install requirements
    with prefix('source /home/api/context/context/bin/activate'):
        run('pip install -r /home/api/context/api/requirements.txt')

        with cd('/home/api/context/api'):
            # Git pull
            run('git pull origin master')

        with cd('/home/api/context/api/app'):
            # Collect all the static files
            run('python manage.py collectstatic')
            # Migrate and Update the database
            run('python manage.py makemigrations')
            run('python manage.py migrate')

        # Restart the nginx server
        run('supervisorctl restart gunicorn')
