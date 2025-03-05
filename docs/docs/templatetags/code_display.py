import html

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def display_code(value):
    """Escapes HTML and Django template tags for safe display"""
    return mark_safe(html.escape(value))
