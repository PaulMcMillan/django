from __future__ import absolute_import

from ..views import BrokenException

from django import template


register = template.Library()

@register.simple_tag
def go_boom(arg):
    raise BrokenException(arg)

