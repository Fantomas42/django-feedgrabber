"""Urls for python_django.feedgrabber authors"""
from django.conf.urls.defaults import *

from feedgrabber.models import Author

author_conf = {'queryset': Author.objects.all()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           author_conf, 'feedgrabber_author_list'),
                       )

urlpatterns += patterns('feedgrabber.views.authors',
                        url(r'^(?P<slug>[-\w]+)/$', 'view_author_detail',
                            name='feedgrabber_author_detail'),
                        )
