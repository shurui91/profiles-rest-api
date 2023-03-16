# profiles-rest-api

## ssh to the server, then go to the correct file path/location
`vagrant ssh`
`cd /vagrant`

## activate the virtual environment
`source ~/env/bin/activate`

## django start a project
`django-admin.py startproject profiles_project .`

## django start an app
`python manage.py startapp profiles_api`

## run the app
`python manage.py runserver 0.0.0.0:8000`