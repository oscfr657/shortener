
from django.conf.urls import patterns, url

from .views import index, shorturl


urlpatterns = patterns('',
                       url(r'^(?P<word>[0-9a-zA-Z]+)/', shorturl, name='shorturl'),
                       url(r'^$', index, name='index'),
                       )