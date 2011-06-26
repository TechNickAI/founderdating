from django import template
import re

register = template.Library()

@register.filter(name='first_word')
def first_word(value):
    return re.sub(' .+', '', value)
