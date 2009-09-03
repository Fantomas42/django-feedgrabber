"""Urls for feedgrabber languages"""
from django.conf.urls.defaults import *

urlpatterns = patterns('feedgrabber.views.languages',
                       url(r'^$', 'view_language_list',
                           name='feedgrabber_language_list'),
                       url(r'^(?P<language>\w+)/$', 'view_language_detail',
                           name='feedgrabber_language_detail'),
                        )
