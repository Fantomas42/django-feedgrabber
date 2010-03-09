"""Admin for feedgrabber"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from feedgrabber.models import Site
from feedgrabber.models import Feed
from feedgrabber.models import Item
from feedgrabber.models import Author
from feedgrabber.models import Category

class FeedInline(admin.TabularInline):
    model = Feed
    extra = 1

class SiteAdmin(admin.ModelAdmin):
    inlines = [FeedInline,]
    list_display = ('name', 'url', 'language', 'description')
    list_filter = ('language',)
    search_fields = ('url', 'name', 'description', 'language')
    fieldsets = ((None, {'fields': ('name', 'url')}),
                 (_('Informations'), {'fields': ('language', 'description')}))

admin.site.register(Site, SiteAdmin)

class FeedAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('site', 'name', 'url', 'creation_date',
                    'get_len_items', 'last_access', 'is_update')
    list_filter = ('site', 'creation_date', 'last_access')
    search_fields = ('url', 'name', 'description')
    fieldsets = ((None, {'fields': ('site', 'url')}),
                 (_('Informations'), {'fields': ('name', 'description',
                                                 'last_access')}))

admin.site.register(Feed, FeedAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website', 'slug')
    search_fields = ('name', 'email', 'website')
    fields = ('name', 'slug', 'email', 'website')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'scheme', 'slug')
    search_fields = ('name', 'scheme')
    fields = ('name', 'slug', 'scheme')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('title', 'feed', 'get_author', 
                    'publication_date', 'is_recent')
    list_filter = ('feed', 'creation_date', 'publication_date')
    search_fields = ('url', 'title', 'content', 'guid', 'comments')
    fieldsets = ((None, {'fields': ('feed', 'url')}),
                 (_('Content'), {'fields': ('title', 'content')}),
                 (_('Additional Content'), {'fields': ('guid', 'author', 'categories',
                                                       'ressource', 'comments')}),
                 (_('Informations'), {'fields': ('creation_date', 'publication_date')}))


admin.site.register(Item, ItemAdmin)
