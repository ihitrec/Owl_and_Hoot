from django import template
register = template.Library()


@register.filter
def list_index(list):
    """Loop trough list within a nested loop, don't alter it for reuse."""

    list.append(list[0])
    return list.pop(0)
