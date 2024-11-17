from django import template
from django.forms import BoundField

register = template.Library()

@register.filter
def add_class(field, cls):
    if isinstance(field, BoundField):
        return field.as_widget(attrs={'class': cls})
    return field