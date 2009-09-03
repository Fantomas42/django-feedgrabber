"""Urls for python_django.feedgrabber feeds"""
from django.conf.urls.defaults import *

from feedgrabber.models import Feed

# Actually use a filter to the admin
urlpatterns = patterns('django.views.generic.simple',                       
                       url(r'^(?P<object_id>\d+)/$', 'redirect_to',
                           {'url': '/admin/feedgrabber/item/?feed__id__exact=%(object_id)s'},
                           'feedgrabber_feed_detail'),
                       )

urlpatterns += patterns('feedgrabber.views.feeds',
                        url(r'^grab/(?P<object_id>\d+)/$', 'view_feed_grab',
                            name='feedgrabber_feed_grab'),
                        )
