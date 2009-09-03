"""Models for feedgrabber"""
import feedparser
from datetime import datetime
from datetime import timedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.template.defaultfilters import linebreaks
from django.template.defaultfilters import slugify

from feedgrabber.settings import UPDATE_HOUR_LIMIT
from feedgrabber.settings import RECENT_HOUR_LIMIT
from feedgrabber.settings import USER_AGENT

class Site(models.Model):
    """Site model"""
    LANGUAGE_CHOICES = settings.LANGUAGES
    
    url = models.CharField(_('url'), max_length=200, unique=True)
    name = models.CharField(_('website'), max_length=200)
    language = models.CharField(_('language'), max_length=20, choices=LANGUAGE_CHOICES)
    description = models.TextField(_('site description'), blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('feedgrabber_site_detail', (self.pk,))

    class Meta:
        verbose_name = _('site')
        verbose_name_plural = _('sites')
        ordering = ('name',)

class Feed(models.Model):
    """Feed model"""
    url = models.CharField(_('url'), max_length=300, unique=True)
    name = models.CharField(_('name'), max_length=300, default=_('not defined'))
    description = models.TextField(_('site description'), blank=True)

    site = models.ForeignKey(Site, verbose_name=_('site'))

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    last_access = models.DateTimeField(_('last access'), blank=True, null=True)

    def __unicode__(self):
        if not self.name or self.name == _('not defined'):
            return self.url
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('feedgrabber_feed_detail', (self.pk,))

    def get_len_items(self):
        return self.item_set.count()
    get_len_items.short_description = _('len items')

    def is_update(self):
        if not self.last_access:
            return False
        return self.last_access + timedelta(hours=UPDATE_HOUR_LIMIT) > datetime.now()
    is_update.boolean = True
    is_update.short_description = _('is update')

    def grab(self):
        """Grab the feed"""
        data = feedparser.parse(self.url, agent=USER_AGENT)

        if data.feed.title and data.feed.title != self.name:
            self.name = data.feed.title
        if data.feed.description and data.feed.description != self.description:
            self.description = data.feed.description

        for entry in data.entries:
            try:
                Item.objects.get(feed=self, guid=entry.link)
            except Item.DoesNotExist:
                item = Item(feed=self)
                item.fill(entry)
                
        self.last_access = datetime.now()
        self.save()

    class Meta:
        verbose_name = _('feed')
        verbose_name_plural = _('feeds')
        ordering = ('creation_date',)

class Author(models.Model):
    """Author model"""
    name = models.CharField(_('name'), max_length=150)
    slug = models.SlugField(_('author slug'))
    website = models.CharField(_('author website'), max_length=150, blank=True)
    email = models.CharField(_('email'), max_length=150, blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('feedgrabber_author_detail', (self.slug,))

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
        ordering = ('name',)

class Category(models.Model):
    """Category model"""
    name = models.CharField(_('name'), max_length=150)
    slug = models.SlugField(_('category slug'))
    scheme = models.CharField(_('scheme'), max_length=150, blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('feedgrabber_category_detail', (self.slug,))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('name',)

class Item(models.Model):
    """Item model"""
    feed = models.ForeignKey(Feed, verbose_name=_('feed'))
    url = models.CharField(_('url'), max_length=300, unique=True)
    
    title = models.CharField(_('title'), max_length=300)
    content = models.TextField(_('content'))
    guid = models.CharField(_('guid'), max_length=300, blank=True)

    author = models.ForeignKey(Author, verbose_name=_('author'),
                               blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True)

    ressource = models.CharField(_('ressource'), max_length=300, blank=True)
    comments = models.CharField(_('comments'), max_length=300, blank=True)

    creation_date = models.DateTimeField(_('creation date'))
    publication_date = models.DateTimeField(_('publication date'))

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('feedgrabber_item_detail', (self.pk,))

    def get_content(self):
        if not '</p>' in self.content:
            return linebreaks(self.content)
        return self.content

    def get_author(self):
        if self.author:
            return self.author.name
        return _('not known')
    get_author.short_description = _('author')
    
    def is_recent(self):
        return self.publication_date + timedelta(hours=RECENT_HOUR_LIMIT) > datetime.now()
    is_recent.boolean = True
    is_recent.short_description = _('is recent')

    def fill(self, entry):
        """Fill the from with the entry"""
        self.url = entry.link
        self.title = entry.title
        self.content = entry.get('summary') or entry.get('subtitle', _('not defined'))
        self.guid = entry.link
        self.ressource = len(entry.get('enclosures', [])) and entry.enclosures[0].href or ''
        self.comments = entry.get('comments', '')
        self.publication_date = datetime(*entry.date_parsed[:7])
        self.creation_date = datetime.now()
        
        if entry.get('author_detail'):
            author, created = Author.objects.get_or_create(name=entry.author_detail.get('name'),
                                                           slug=slugify(entry.author_detail.get('name')),
                                                           email=entry.author_detail.get('email', ''),
                                                           website=entry.author_detail.get('href', ''))
            self.author = author
        self.save()
        
        for tag in entry.get('tags', []):
            scheme = ''
            if tag.scheme:
                scheme = tag.scheme
            category, created = Category.objects.get_or_create(name=tag.term, slug=slugify(tag.term),
                                                               scheme=scheme)
            self.categories.add(category)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('-publication_date', 'feed')
