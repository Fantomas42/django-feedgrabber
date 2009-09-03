"""Urls for feedgrabber syndication"""
from django.conf.urls.defaults import *

from feedgrabber.feeds import LatestItems
from feedgrabber.feeds import TopRatedItems

feeds = {'latest': LatestItems,
         'toprated': TopRatedItems}

urlpatterns = patterns('',
                       url(r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
                           {'feed_dict': feeds}, 'feedgrabber_syndication'),
                       )
