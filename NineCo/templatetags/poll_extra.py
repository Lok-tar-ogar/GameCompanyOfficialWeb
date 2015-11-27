from django import template

register = template.Library()


@register.filter(name='shorterArt')
def shorterArt(value, arg):
    return value[:arg]
