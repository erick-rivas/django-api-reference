# Django API

This repository holds the source code of a **reference** for the development of a **Django api** written mainly in python.

## Architecture design

The reference uses a architecure based on a Generic Model View pattern, Inspired by the architecture of [Django framework](https://www.djangoproject.com) and [Django REST framework](https://www.django-rest-framework.org)

### General description

In general terms, the architecture uses the following structure:

  - /app: App general settings
    - api.py: Api routes definitions
    - settings.py: App settings (dependencies, configurations, etc)
  - /models: Model definitions [More info](https://docs.djangoproject.com/en/2.1/topics/db/models/)
  - /serializers: Model serializers [More info](https://www.django-rest-framework.org/api-guide/serializers/)
  - /views: Api views [More info](https://www.django-rest-framework.org/api-guide/views/)

## Pre-requisites:

 * Download & install [Python3](https://www.python.org/downloads/)
 * Download & install [PyCharm CE](https://www.jetbrains.com/pycharm/download/)

### To start coding and build:

 * Clone this repository.
 * Install postgresql database.
 * Create virtual environment
  ```bash
 $ python3 -m venv .venv
 $ . .venv/bin/activate
 ```
 * Open project in PyCharm
 * Go to PyCharm > Preferences > Project interpreter > Add > Select <project_dir>/venv
 * Install dependencies (Suggested in PyCharm Terminal)
 ```bash
(.env)$ pip3 install -r requirements.txt
 ```
 * Set database settings in app/settings.py
 * Create a new database with the name shown in the last step
 * Make migrations
 ```bash
(.venv)$ python3 manage.py makemigrations
 ```
 * Run migrations
 ```bash
(.venv)$ python3 manage.py migrate
 ```
 * Run project
```bash
(.venv)$ python3 manage.py runserver
 ```

 ### To enable admin panel

 * Add models to /app/admin
 * Create superuser
 ```bash
(.venv)$ python3 manage.py createsuperuser
 ```
 * Open admin panel 
 ```bash
 http://localhost:8080/admin
 ```
 
 ### To enable authentication
 
 * Go to views/helpers/viewsets.py and uncomment
 ```bash
authentication_classes = (TokenAuthentication,)
permission_classes = (IsAuthenticated,)
 ```
 * To test generate token
 ```bash
(.venv)$ python3 manage.py drf_create_token <superuser_username>
 ```
 * Send request
 ```bash
$ curl -i -X GET http://127.0.0.1:8000/api/players -H 'Authorization: Token <Token>'
 ```
 
 ### Examples

 * Example docs.
 ```bash
 http://localhost:8080/docs
 ```
  * Example requests. 
 ```bash
 GET http://localhost:8080/v1/players
 ```
 
 
## Deploy to aws eb

### Configure aws/dns console

* Open aws elastic beanstalk console and create an environment 
> Important: Configure apache as proxy server and enable 443 port in security groups

* Configure a postgresql database settings in aws console (settings/databases/modify)

* Configure DNS settings in domain provider, e.g *godaddy*


### Configure server

* Install eb and configure credentials, See ([install](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install.html) & [credentials](https://docs.aws.amazon.com/es_es/general/latest/gr/managing-aws-access-keys.html))

* Init eb project
```bash
$ eb init
 ```

* Enable ssh
```bash
$ eb ssh --setup
 ```

* Execute ssh and setup apache settings
```bash
$ sudo vim /etc/httpd/conf.d/temp.conf
# Listen 80
# <VirtualHost *:80 *:443>
# 	ServerName <HTTPS_DOMAIN>
# 	DocumentRoot /var/www/html
# </VirtualHost>
```

* Install and configure certbot
```bash
$ sudo wget https://dl.eff.org/certbot-auto
$ sudo chmod a+x ./certbot-auto
$ sudo ./certbot-auto certonly --debug --webroot
# root: /var/www/html
$ sudo ./certbot-auto certonly --debug
```
* Set HTTPS_DOMAIN in .ebextensions/django.config

### Deploy

* Set DEBUG = FALSE in app/settings.py

* Generate static files (autogenerated)
```bash
(.venv)$ python3 manage.py collectstatic
 ```
 
 * Make database migrations
 
 * Deploy to aws
```bash
$ eb deploy
 ```