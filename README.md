# Django API

This repository holds the source code of a **reference** for the development of a **Django api** written mainly in python.

## Table of content

-  [Overview](#overview)
-  [Pre-requisites](#pre-requisites)
-  [Installation](#installation)
    -  [Filling of database](#filling-of-database)
    -  [Test running](#test-running)
-  [Examples](#examples)
-  [Deployment](#deployment)
    
## Overview

The reference uses a architecture based on a Generic Model View pattern, Inspired by the architecture of [Django framework](https://www.djangoproject.com) and [Django REST framework](https://www.django-rest-framework.org).

In general terms, the architecture uses the following structure:

-  /app: General settings of api.
   -  api.py: Api routes definitions.
   -  settings.py: App settings (dependencies, configurations, etc).
-  /domain: Business logic methods. [More info](./domain/__guides.md)
-  /fixtures: Preloaded data definitions.
-  /models: Model definitions. [More info](./models/__guides.md)
-  /mutations: Graphql mutations 
-  /schema: Graphql schema & types
-  /seed: Autogenerated files (builder).
-  /serializers: Model serializers. [More info](./serializers/__guides.md)
-  /views: Api route definitions. [More info](./views/__guides.md).

## Pre-requisites

-  Download & install [Python3](https://www.python.org/downloads/).
-  Download & install [PyCharm CE](https://www.jetbrains.com/pycharm/download/).

## Installation

-  Clone this repository.
-  Install postgresql database.
-  Run install script.
```bash
$ ./bin/install
```

- Install builder
```bash
$ npm install -g seed-builder
```

-  Configure .env.dev file attributes.
-  Create a new database with the name shown in the last step.
-  Make migrations.
```bash
(.venv)$ python3 manage.py makemigrations
```

-  Run migrations.
```bash
(.venv)$ python3 manage.py migrate
```

-  Run project.
```bash
(.venv)$ python3 manage.py runserver
```

### Filling of database 

-  Load fixtures.
```bash
(.venv)$ python3 manage.py loaddata fixtures/*.yaml
```

### Test running

-  Run domain test cases.
```bash
(.venv)$ python3 manage.py test domain/tests/
```


## Examples

-  Execute api request.
```bash
GET http://localhost:8000/api/players
```

-  Execute graphql request.
```bash
GET http://localhost:8000/graphql
```

-  Open admin pane.
```bash
http://localhost:8000/admin
```
> To access admin pane, create a user fixture with *is_superuser* attribute set to true 


## Deployment

-  To deploy application to aws see [deployment](./bin/deployment.md).
