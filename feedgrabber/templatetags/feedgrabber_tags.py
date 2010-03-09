"""Templatetags for getting the items grabbed"""
from django.template import Library
from django.template import Node
from django.template import TemplateSyntaxError

from feedgrabber.models import Item

register = Library()

class LatestItemNode(Node):
    """Node setting the latest items"""
    def __init__(self, num, varname):
        self.num, self.varname = int(num), varname

    def render(self, context):
        context[self.varname] = Item.objects.all()[:self.num]
        if self.num == 1:
            context[self.varname] = context[self.varname][0]
        return ''


@register.tag
def get_latest_items(parser, token):
    """{% get_latest_item n as var %}"""
    bits = token.split_contents()

    if len(bits) != 4:
        raise TemplateSyntaxError, "get_latest_item tag takes exactly three arguments"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "second argument to get_latest_item tag must be 'as'"
    return LatestItemNode(bits[1], bits[3])
    



