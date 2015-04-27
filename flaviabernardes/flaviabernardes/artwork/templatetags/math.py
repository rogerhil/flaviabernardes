from django import template
register = template.Library()

@register.filter
def mul(value, arg):
    value = int(value)
    arg = int(arg)
    return value * arg
