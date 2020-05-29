from django import template

register = template.Library()

@register.filter
def as_percentage_of(part, whole):
    try:
        value = (part / whole)
        return '{0:.2%}'.format(value)
    except (ValueError, ZeroDivisionError):
        return ""