# Django-jwt


<h3 align='center'> To run the project</h3>

---
```
$ git clone https://github.com/SreekanthTeja/django-jwt.git
$ virtualenv env
$ source env/bin/activate
$ cd <project name>
$ python manage.py migrate
$ python manage.py runserver
```
---

<h4 align='center'>Postman Testing</h4>

> to register the users
```
$ localhost:8000/auth/users/
```
> to activate the users
```
$ localhost:8000/auth/users/activation/
```
> to login the users
```
$ localhost:8000/auth/jwt/create/
```
