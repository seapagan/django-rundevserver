# django-rundevserver

[![PyPI version](https://badge.fury.io/py/django-rundevserver.svg)](https://badge.fury.io/py/django-rundevserver)

A simple [Django][django] addon to provide a new management command which runs a
development server with custom host/port set in the applications `settings.py`
file. You can also set the DEBUG variable here, allowing the default setting to
be False for production.

## Installation

Install the addon using pip:

```bash
pip install django-rundevserver
```

__OR__, if you have forked this repository to your local machine, you can build the
package using the following steps:

```bash
pip install -r requirements.txt
python setup.py sdist
pip install dist/django-rundevserver-0.3.tar.gz
```

This implies your Python and Pip commands are as above, substitute your own
versions if different.

## Usage

Add this app to your Django settings.py INSTALLED_APPS like any other:

```python
INSTALLED_APPS = [
        ...
        'rundevserver',
    ]
```

Now, just use `rundevserver` instead of `runserver`:

```bash
python manage.py rundevserver
```

By default, this will function exactly as the standard `runserver` except it
__automatically enables the DEBUG setting.__ In this way, you can leave
`DEBUG=False` in your main `settings.py` file so it is correct for production,
but during development or debugging it will be set to True.

Configuration variables are set in the project `settings.py` and current accepted
values are as below. If all of these are unspecified, `rundevserver` will function
exactly as `runserver` (except for the aforementioned DEBUG setting!):

```python
# Chose which port to listen to, defaults to 8000 if unspecified
RDS_PORT = 8001

# Listen on all interfaces (ie 0.0.0.0) if true. Otherwise (or if unspecified),
# it will use the standard 127.0.0.1.
RDS_ALL_INTERFACES = True

# Force DEBUG mode if True OR unspecified. If you dont want DEBUG set in
# development for some reason, specifiy False here
RDS_DEBUG = True
```

`RDS_ALL_INTERFACES` is very useful if you are developing on a remote machine
where the default runserver localhost would not let you connect.

## Todo

* Add documentation
* Add Tests

[django]: https://www.djangoproject.com/
