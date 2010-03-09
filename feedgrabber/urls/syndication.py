"""Urls for feedgrabber syndication"""
from django.conf.urls.defaults import *

from feedgrabber.feeds import LatestItems

feeds = {'latest': LatestItems,}

urlpatterns = patterns('',
                       url(r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
                           {'feed_dict': feeds}, 'feedgrabber_syndication'),
                       )
