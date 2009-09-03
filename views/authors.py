"""Views for python_django.feedgrabber authors"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from feedgrabber.models import Author


def view_author_detail(request, slug):
    """Detail view for the author"""
    author = get_object_or_404(Author, slug=slug)
    return object_list(request, queryset=author.item_set.all(),
                       extra_context={'author': author})


