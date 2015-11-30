from django import template

register = template.Library()


@register.filter(name='shorterArt')
def shorterArt(value, arg):
	Spacestr = ''
    if len(value) > int(arg):
    	Spacestr='...'
    return value[:arg]+Spacestr
