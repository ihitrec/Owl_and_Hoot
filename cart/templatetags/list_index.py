from django import template
register = template.Library()


list = []


@register.filter
def list_index(indexable):
    """Loop trough list within a nested loop, don't alter it for reuse."""

    global list
    list = indexable
    list.append(list[0])
    return list.pop(0)
