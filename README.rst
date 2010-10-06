==================
Django-Feedgrabber
==================

Django-feedgrabber is a django application which grabs RSS/Atom feeds
throught the network, for archiving and displaying the feeds with
categorization.

.. contents::

Install
=======

Install the package in your *PYTHON_PATH* by getting the sources and run
**setup.py** or use *pip* ::

  $> pip install -e git://github.com/Fantomas42/django-feedgrabber.git#egg=django-feedgrabber

Then register the **feedgrabber** app in your *INSTALLED_APPS* project's
section.

Urls
====

Multiple urlsets are provided to ensure the navigation. ::

  >>> url(r'^friendfeeds/', include('feedgrabber.urls.items')),
  >>> url(r'^friendfeeds/feeds/', include('feedgrabber.urls.feeds')),
  >>> url(r'^friendfeeds/authors/', include('feedgrabber.urls.authors')),
  >>> url(r'^friendfeeds/languages/', include('feedgrabber.urls.languages')),
  >>> url(r'^friendfeeds/categories/', include('feedgrabber.urls.categories')),

Command
=======

Feedgrabber provide one django command for grabbing the feeds. Execute it
as a cronjob to refresh yours feeds. ::

  $> python manage.py grabfeeds

