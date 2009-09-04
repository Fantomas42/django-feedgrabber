"""Sitemaps for feedgrabber"""
from django.contrib.sitemaps import Sitemap

from feedgrabber.models import Item

class ItemSitemap(Sitemap):
    """Sitemap for feedgrabber.item"""
    priority = 0.5

    def items(self):
        return Item.objects.all()
    
    def lastmod(self, obj):
        return obj.creation_date
                         
    
