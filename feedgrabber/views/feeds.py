"""Views for feedgrabber feeds"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from feedgrabber.models import Feed

def view_feed_grab(request, object_id):
    """Grab the feed and display the items"""
    feed = get_object_or_404(Feed, pk=object_id)
    feed.grab(request.user)
    request.user.message_set.create(message=_('The feed has been grabbed.'))
    return HttpResponseRedirect(feed.get_absolute_url())
    
