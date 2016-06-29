from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    return value.replace(arg, '')
