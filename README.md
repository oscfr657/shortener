shortener
=========

A django app to shorten urls.


Quick start
-----------

1. Add "urlshortener" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'urlshortener',
    )

2. Include the urlshortener URLconf in your project urls.py like this::

    url(r'', include('urlshortener.urls')),

3. Run `python manage.py migrate` to create the urlshortener models.


