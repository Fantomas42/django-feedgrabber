"""Urls for feedgrabber categories"""
from django.conf.urls.defaults import *

from feedgrabber.models import Category

category_conf = {'queryset': Category.objects.all()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           category_conf, 'feedgrabber_category_list'),
                       )

urlpatterns += patterns('feedgrabber.views.categories',
                        url(r'^(?P<slug>[-\w]+)/$', 'view_category_detail',
                            name='feedgrabber_category_detail'),
                        )
