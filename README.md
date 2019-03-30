# create-automatic-api
Generating API automatically with Django

* Create virtual environment:
```bash
virtualenv venv -p C:\Python36\python.exe
.\venv\Scripts\activate
```

* Install packages
```bash
pip3 install django djangorestframework drf-generators
```

* Auto generate requirements.txt 
```bash
$ pip3 freeze > requirements.txt
```

* Create Django project:
```bash
django-admin startproject config .
python .\manage.py startapp bills
```

* Include new apps in settings.py:
```python
INSTALLED_APPS = [
 ‘django.contrib.admin’,
 ‘django.contrib.auth’,
 ‘django.contrib.contenttypes’,
 ‘django.contrib.sessions’,
 ‘django.contrib.messages’,
 ‘django.contrib.staticfiles’,
 ‘bills’,
 ‘rest_framework’,
 ‘drf_generators’,
]
```

* Create sqlite3 database
```bash
python .\manage.py migrate
```

* Sqlite3 database schema:
```sql
CREATE TABLE bill (
    id             INTEGER        PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    name           VARCHAR (255)  NOT NULL,
    date           DATETIME       NOT NULL,
    ident_category INTEGER        NOT NULL
                                  REFERENCES category (id),
    price          DECIMAL (7, 2) DEFAULT (0),
    comment        TEXT
);

CREATE TABLE category (
    id        INTEGER       PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
    name      VARCHAR (255) NOT NULL,
    operation INTEGER       NOT NULL
);
```

* Generate django models
```bash
python .\manage.py inspectdb bill category > .\bills\models.py
```

* Register classes in admin.py
```python
from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('bills')

for model_name, model in app.models.items():
    admin.site.register(model)
```

* Create superuser:
```
python .\manage.py createsuperuser
```

* Create migrations and apply:
```bash
python .\manage.py makemigrations
python .\manage.py migrate
```

* Fix config/urls.py:
```python
urlpatterns = [
  path(‘admin/’, admin.site.urls),
  path(‘’, include(bills.urls’)),
]
```

* Define Pagination in settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15
}
```

* Run server
```bash
python .\manage.py runserver
```

* Usage
GET http://127.0.0.1:8000/bills/1

JSON Result: 
```
{"id":1,"name":"Comida","date":"2019-03-30T13:54:11Z","price":"9.87","comment":"Almoço","ident_category":1}
```

GET http://127.0.0.1:8000/category/?format=json

JSON Result: 
```
{"count":2,"next":null,"previous":null,"results":[{"id":1,"name":"Despesa","operation":0},{"id":2,"name":"Receita","operation":1}]}
```
