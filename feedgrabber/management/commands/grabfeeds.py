"""GradFeeds command"""
from django.conf import settings
from django.core.management.base import NoArgsCommand

from feedgrabber.models import Feed
from feedgrabber.models import Item

class Command(NoArgsCommand):
    """Grabbing feeds and stock it"""

    def handle_noargs(self, **options):
        feeds = [f for f in Feed.objects.all() if not f.is_update()]
        feeds_len = len(feeds)
            
        for i in range(feeds_len):
            feed = feeds[i]
            print 'Grabbing feed %i/%i %s...' % (i + 1, feeds_len, feed.url)
            feed.grab()
