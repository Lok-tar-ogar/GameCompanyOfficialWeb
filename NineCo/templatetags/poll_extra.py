from django import template

register = template.Library()


@register.filter(name='shorterArt')
def shorterArt(value, arg):
    return value[:arg]+'...' if len(value)>30 else value[:arg]


@register.filter(name='NewsFilter')
def NewsFilter(value, arg):
	return value[:arg]+'...' if len(value)>17 else value[:arg]