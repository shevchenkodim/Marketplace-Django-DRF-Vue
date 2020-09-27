from django import template
register = template.Library()


@register.inclusion_tag('tags/paginator.html')
def paginator_tag():
    return {}
