# pylint: disable=no-member
from products.models import Product


def cart_items(request):
    """Get products, individual prices and total cart price"""

    cart = request.session.get('cart', {})

    cart_items = {}
    for product in cart:
        cart_items[Product.objects.get(id=product)] = cart[product]

    prices = []
    for product, value in cart_items.items():
        for num in value.values():
            prices.append(product.price*num)
    total = sum(prices)

    context = {
        'cart_items': cart_items,
        'prices': prices,
        'total': total
    }
    return context
