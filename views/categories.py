"""Views for python_django.feedgrabber categories"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from feedgrabber.models import Category


def view_category_detail(request, slug):
    """Detail view for the category"""
    category = get_object_or_404(Category, slug=slug)
    return object_list(request, queryset=category.item_set.all(),
                       extra_context={'category': category})


