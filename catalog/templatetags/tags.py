from django import template

register = template.Library()

@register.filter()
def media(value):
    if value:
        return f'/media/{value}'
    return '#'