# pylint: disable=no-member
from products.models import Product


def cart_items(request):

    updated = False

    # Update specific item qty or remove it from cart, change updated
    if request.method == "POST":
        if 'cart-update' in request.POST:
            request.session['cart'][request.POST.get('cart-update')][request.POST.get('size')] = int(request.POST.get('quantity'))
            request.session.modified = True
            updated = True
        elif 'cart-remove' in request.POST:
            product = request.session['cart'][request.POST.get('cart-remove')]
            del product[request.POST.get('size')]
            if not product:
                del request.session['cart'][request.POST.get('cart-remove')]
            request.session.modified = True
            updated = True


    # Get products, individual prices, total cart price and quantity
    cart = request.session.get('cart', {})

    cart_items = {}
    for product in cart:
        cart_items[Product.objects.get(id=product)] = cart[product]

    quantity = 0
    prices = []
    for product, value in cart_items.items():
        for num in value.values():
            prices.append(product.price*num)
            quantity += num
    total = sum(prices)

    context = {
        'cart_items': cart_items,
        'prices': prices,
        'total': total,
        'quantity': quantity,
        'updated': updated
    }
    return context
