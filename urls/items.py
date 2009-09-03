"""Urls for python_django.feedgrabber items"""
from django.conf.urls.defaults import *

from feedgrabber.models import Item

item_conf = {'queryset': Item.objects.all()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           item_conf, 'feedgrabber_item_list'),
                       url(r'^(?P<object_id>\d+)/$', 'object_detail',
                           item_conf, 'feedgrabber_item_detail'),
                       )

