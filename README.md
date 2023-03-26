# profiles-rest-api

## ssh to the server, then go to the correct file path/location
`vagrant ssh`
`cd /vagrant`

## create a virtual environment called `venv`
`python3 -m venv ~/venv`

## activate the `venv` virtual environment
`source ~/venv/bin/activate`

## django create a project
`django-admin.py startproject profiles_project .`

## django create an app
`python manage.py startapp profiles_api`

## run the app
`python manage.py runserver 0.0.0.0:8000`
