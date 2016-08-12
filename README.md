# Activities-browser Django
TrixDiscover

![Image of TrixDiscover](https://github.com/pauEscarcia/Activities-browser/blob/master/media/TrixDiscover.png)



:two_hearts: 
### What is TrixDiscoverCMS?
Have you ever been in a magic place? That wonderful place where you 
experienced a kind of feeling you never felt before. We help you to plan the best travel experience of your life while unveiling the hidden treasures of this beautiful country.  Discover that feeling, enjoy **TrixDiscover**.
### Try something different
**TrixDiscover** offers the best option to explore the rustic tourism offer in Mexico.
Personalize your next adventure in Mexico according to your personal taste, your travel preferences, and even your previous trips.

##Technology versions
Technology versions to use for the development:

* Database: Postgresql v9.5
* Programming language: Python v2.7
* Python Framework CMS: Django v1.9.8
* CMS Django v3.3.1

##Getting Started with django CMS 
1. Creating the virtual environment
`virtualenv env`
2. Activate the virtual environment
`env\Scripts\activate`
3. Install django
`pip install django==1.9.8` 
4. Creating proyect 
`django-admin.py startproyect mysite .`
5. Run the proyect 
`python manage.py runserver` 

##Migrate a project from sqlite3 to postgresql
* Configure the settings.py file
```
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'TrixDiscover',
         'USER': 'trixDiscover',
         'PASSWORD': 'root',
         'HOST': 'localhost',
         'PORT': '5432',

    }
}
```
* Psycopg is a PostgreSQL adapter for the Python programming language. It is a wrapper for the libpq.
 `pip install psycopg2` 
* `python manage.py migrate`
* `python manage.py runserver`

##Create a model in Django
In the following image modeling database to trixdiscovercms where relationships between tables ( As we know will create modeling within an application django ) is shown . It's just to learn how to do it.
![Model](https://github.com/pauEscarcia/ActivitiesBrowser/blob/master/images/bd.png)



