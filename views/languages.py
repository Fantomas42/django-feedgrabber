"""Views for feedgrabber languages"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.conf import settings

from feedgrabber.models import Item

LANGUAGES = dict(settings.LANGUAGES)

# DO something more efficient in the future
def view_language_list(request):
    """Detail view for the language"""
    return render_to_response('feedgrabber/language_list.html',
                              {'languages': LANGUAGES},
                              context_instance=RequestContext(request))


def view_language_detail(request, language):
    """Detail view for the language"""
    items = Item.objects.filter(feed__site__language__iexact=language)
    return object_list(request, queryset=items,
                       extra_context={'language_code': language,
                                      'language_trans': LANGUAGES[language]})

