# context

Giving context to news articles

### Setup

We utilize [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) as a virtual environment wrapper. Follow the installation instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html). After this installs do `mkvirtualenv context`. This will put you in a virtualenv for `context`. When you open up a new shell you can do `workon context`, and to deactivate this virtual environment do `deactivate`.

Then go ahead and run `pip install -r requirements.txt` to install the dependencies.

On our development environment we use Postgres. Install Postgres through either [Postgres.app](http://postgresapp.com/) or [Postgresql.org](http://www.postgresql.org/download/).

After installing Postgres in `psql` run `CREATE USER context WITH PASSWORD 'LnmEksnM36uPHG';`, and then run `CREATE DATABASE context OWNER context;`.

Then you can run `./manage.py migrate`, and `./manage.py runserver`.

Make yourself a user & an admin by running `./manage.py shell` then:

```
>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('username', password='123')
>>> user.is_superuser=True
>>> user.is_staff=True
>>> user.save()
```
