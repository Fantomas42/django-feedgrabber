"""Urls for feedgrabber items"""
from django.conf.urls.defaults import *

from feedgrabber.models import Item
from feedgrabber.settings import PAGINATION

item_conf = {'queryset': Item.objects.all(),
             'paginate_by': PAGINATION}

item_conf_detail = {'queryset': Item.objects.all(),}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           item_conf, 'feedgrabber_item_list'),
                       url(r'^page/(?P<page>\d)/$', 'object_list',
                           item_conf, 'feedgrabber_item_list_paginated'),                       
                       url(r'^(?P<slug>[-\w]+)/$', 'object_detail',
                           item_conf_detail, 'feedgrabber_item_detail'),
                       )

