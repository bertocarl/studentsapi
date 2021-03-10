# Django Rest Framework Authentication with Dj-Rest-Auth

This repository is an Authentication and authorization in Django RESTful APIs using Dj-Rest-Auth with Gmail server for sending verification emails to users. 

## To Run on Localhost:

- Have `Python` and `pip` installed on your local machine

## Running the Django project:

Create an isolated environment for the project with `virtualenv`. You can install `virtualenv` with the following command:

```
sudo pip install virtualenv
```

Create a new directory for the project:

```
mkdir myproject && cd myproject
```

Create a virtual environment for the project:

```bash
virtualenv env
```

Then, activate it:

```bash
source env/bin/activate
```



Install Django and Django REST Framework:

```bash
pip install django djangorestframework
```

Finally, `cd` into the _studentapi_ folder and run the project:

```bash
python manage.py runserver
```

Go to http://localhost:8000/ to see if the API is up and running.


