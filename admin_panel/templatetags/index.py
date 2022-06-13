from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    if indexable:
        return indexable[i]
    else:
        return 0