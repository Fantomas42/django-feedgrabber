"""Feeds for feedgrabber """
from django.core.urlresolvers import reverse
from django.contrib.syndication.feeds import Feed
from django.contrib.syndication.feeds import FeedDoesNotExist

from feedgrabber.models import Item

class ItemFeed(Feed):
    title_template = 'syndication/item_title.html'
    description_template= 'syndication/item_description.html'

    def link(self):
        return reverse('feedgrabber_item_list')

    def items(self):
        return Item.objects.all()

    def item_pubdate(self, item):
        return item.publication_date

class LatestItems(ItemFeed):
    pass

class TopRatedItems(ItemFeed):
    pass
