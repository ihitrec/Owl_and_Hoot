# pylint: disable=no-member
from products.models import Product

updated = False
message = ''


def product_update(request):
    """
    Update product qty or remove it.

    If function called from checkout view,
    changes global updated variable to prevent double call
    """

    try:
        cart = request.session.get('cart', {})
        global updated
        if request.method == "POST":
            if request.session.get('cart'):
                if 'cart-update' in request.POST:
                    cart[request.POST.get('cart-update')][request.POST.get(
                        'size')] = int(request.POST.get('quantity'))
                    request.session.modified = True
                    updated = True
                elif 'cart-remove' in request.POST:
                    try:
                        product = cart[request.POST.get('cart-remove')]
                        del product[request.POST.get('size')]
                        if not product:
                            del cart[request.POST.get('cart-remove')]
                        request.session.modified = True
                        updated = True
                    except KeyError:
                        pass
    except Product.DoesNotExist:
        global message
        message = ("A product from your cart is not available anymore, "
                   "it has been removed.")


def details(request):
    """
    Get products, individual prices, total cart price and quantity.

    Set values as details keys so total can be accessed from the checkout view.
    If product not found in db, notify user and remove from session.
    """

    cart = request.session.get('cart', {})
    cart_items = {}
    removed_product = ''
    for product in cart:
        try:
            cart_items[Product.objects.get(id=product)] = cart[product]
        except Product.DoesNotExist:
            removed_product = product
            global message
            message = ("A product from your cart is not available anymore, "
                       "it has been removed.")

    if removed_product:
        del request.session['cart'][removed_product]
        request.session.modified = True
        removed_product = ''

    quantity = 0
    prices = []
    for product, value in cart_items.items():
        for num in value.values():
            prices.append(product.price*num)
            quantity += num
    total = sum(prices)
    details.cart_items = cart_items
    details.prices = prices
    details.total = total
    details.quantity = quantity


def cart_items(request):
    """Add cart items and details to context"""

    global updated
    if updated is False:
        product_update(request)

    details(request)

    context = {
        'cart_items': details.cart_items,
        'prices': details.prices,
        'total': details.total,
        'quantity': details.quantity,
        'updated': updated,
        'messagew': message
    }

    updated = False

    return context
