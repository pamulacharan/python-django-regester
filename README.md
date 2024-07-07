# python-django-regester


Open Command Prompt:


python --version

pip --version


pip install django

python -m django --version

pip install django

python -m django --version

django-admin startproject myproject
cd myproject


python manage.py startapp accounts


python manage.py migrate

python manage.py runserver

myproject/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── templates/
│   │   └── accounts/
│   │       ├── register.html
│   │       └── register_done.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3




http://127.0.0.1:8000/accounts/register/














