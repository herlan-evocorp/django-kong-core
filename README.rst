=====
Django Kong Core
=====

Django Kong Core é uma aplicação base para transforçar os cabeçalhos da requisição do kong em modelo mapeado.

Quick start
-----------

1. Add "django-kong-core" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kong_core',
    ]

2. Include the middleware in middleware settings.py like this::

    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',        
        'apps.kong_core.middleware.KongClientMiddleware',
        ...
    ]

3. Run `python manage.py migrate` to create the django-kong-core models.

4. enjoy it!
