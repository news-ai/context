# context

Giving context to news articles

### Setup

We utilize [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) as a virtual environment wrapper. Follow the installation instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html). After this installs do `mkvirtualenv context`. This will put you in a virtualenv for `context`. When you open up a new shell you can do `workon context`, and to deactivate this virtual environment do `deactivate`.

Then go ahead and run `pip install -r requirements.txt` to install the dependencies.

On our development environment we use Postgres. Install Postgres through either [Postgres.app](http://postgresapp.com/) or [Postgresql.org](http://www.postgresql.org/download/).

After installing Postgres in `psql` run `CREATE USER context WITH PASSWORD 'LnmEksnM36uPHG';`, and then run `CREATE DATABASE context OWNER context;`.

Also setup the test database: run `ALTER USER context CREATEDB;`, `CREATE DATABASE test_context OWNER context;`. To run tests you can simply do `./manage.py test`.

Then you can run `./manage.py migrate`, and `./manage.py runserver`.

Make yourself a user & an admin by running `./manage.py shell` then:

```
>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('username', password='123')
>>> user.is_superuser=True
>>> user.is_staff=True
>>> user.save()
```

To setup `nltk` go into your python REPL `python` then do `import nltk`, `nltk.download()` (or `nltk.download_shell()` if it hangs).

To setup `redis` follow [this](http://redis.io/topics/quickstart) guide or `brew install redis`. Then run `redis-server`.

### Fabfiles

We use [Fabric](http://fabfile.org/) for deployments. [Here](https://micropyramid.com/blog/automate-django-deployments-with-fabfile/) is a tutorial.

### Docker

Setup using [this](https://github.com/SykoTheKiD/DockerDjangoRest) tutorial.

1. `docker-machine start default`
2. `docker-machine env`
3. `eval $(docker-machine env)`
4. `docker-compose build`
5. `docker-compose up`
6. "Go to your docker machine's IP address and you should see your app"
7. "If the CSS isn't loading run docker-compose run app /usr/local/bin/python manage.py collectstatic and then reload"

### Notes

- End user can only access the `feeds` API endpoint, which has IDs to articles/timelines/etc.
- Articles/timelines don't list the information to the user, but user can look up with an ID.
