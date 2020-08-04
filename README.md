# Onlinevars

## Requirements

Django Admin is installed and activated.

## Quick start

1.  Add "onlinevars" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'onlinevars',
    ]

2.  Include the onlinevars URLconf in your project urls.py like this::

    path('onlinevars/', include('onlinevars.urls')),

3.  Run `python manage.py migrate` to create the models.

4.  Visit <http://127.0.0.1:8000/admin/onlinevars>
