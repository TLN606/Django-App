from django import template

register = template.Library()


@register.filter
def vnd(value):
    """45000 -> '45.000'. Django's locale vi không nhóm hàng nghìn nên tự định dạng."""
    return f'{int(value):,}'.replace(',', '.')
