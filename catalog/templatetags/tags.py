from django import template

register = template.Library()

@register.filter()
def media(value):
    return f'/media/{value}'
