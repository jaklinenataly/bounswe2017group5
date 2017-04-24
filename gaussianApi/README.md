# Installation

Install Django
```shell
$ pip install django
```

Create and activate a virtual environment.
```shell
$ python3 -m venv gauss
$ source gauss/bin/activate
```

Create a project
```shell
$ django-admin startproject apiProject
```

Create the api apps
```shell
$ python manage.py startapp apiApp
```

Create an admin user
```shell
$ python manage.py createsuperuser
$ Username: admin
$ Password: pass12345
```

Create sqlite database.
```shell
$ python manage.py makemigrations
$ python manage.py migrate

```

The development server: to verify your Django project works.
```shell
$ python manage.py runserver

```
Try to show
```shell
http://127.0.0.1:8000/apiApp/
http://127.0.0.1:8000/admin/
```

[Documentation](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)