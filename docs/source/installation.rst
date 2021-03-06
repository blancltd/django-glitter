============
Installation
============


Getting the code
================

The recommended way to install Django Glitter is via pip_::

    $ pip install django-glitter

.. _pip: http://www.pip-installer.org/


settings.py
===========

INSTALLED_APPS
--------------

You'll need to add ``glitter`` to `INSTALLED_APPS`, as well as any app dependencies, or additional
blocks which are included with Glitter as Django apps::

    INSTALLED_APPS = (
        #...

        # Glitter, and recommended packages
        'glitter',
        'glitter.pages',
        'glitter.assets',

        # Standard blocks
        'glitter.blocks.html',
        'glitter.blocks.image',
        'glitter.blocks.redactor',

        # Glitter pages dependencies
        'mptt',
        'django_mptt_admin',
        'sorl.thumbnail',
        'taggit',

        #...
    )

After updating ``INSTALLED_APPS``, you'll need to migrate your database:

.. code:: console

    $ python manage.py migrate


MIDDLEWARE_CLASSES
------------------

Glitter uses ``PageFallbackMiddleware`` as a 404 page handler to render a page if no other view
handles the request, and ``ExceptionMiddleware`` to handle exceptions generated by Glitter views.

You'll need to add these lines to the **bottom** of ``MIDDLEWARE_CLASSES``::

    MIDDLEWARE_CLASSES = [
        #...
        'glitter.pages.middleware.PageFallbackMiddleware',
        'glitter.middleware.ExceptionMiddleware',
    ]


urls.py
=======

The Glitter block admin needs registering in your ``urls.py``::

    from glitter.blockadmin import blocks

    urlpatterns = [
        #...
        url(r'^blockadmin/', include(blocks.site.urls)),
        #...
    ]
