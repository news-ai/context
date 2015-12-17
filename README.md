# context

Giving context to news articles

### Setup

We utilize [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) as a virtual environment wrapper. Follow the installation instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html).

Then go ahead and run `pip install -r requirements.txt` to install the dependencies.

On our development environment we use Postgres. Install Postgres through either [Postgres.app](http://postgresapp.com/) or [Postgresql.org](http://www.postgresql.org/download/).

After installing Postgres in `psql` run `CREATE USER context WITH PASSWORD 'LnmEksnM36uPHG';`, and then run `CREATE DATABASE context OWNER context;`.

Then you can run `./manage.py migrate`, and `./manage.py runserver`.
