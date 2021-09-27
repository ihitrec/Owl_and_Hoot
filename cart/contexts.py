# pylint: disable=no-member
from products.models import Product

updated = False


def product_update(request):
    """
    Update product qty or remove it.

    If function called from checkout view, changes global updated variable to prevent double call
    """

    cart = request.session['cart']
    global updated
    if request.method == "POST":
        if request.session.get('cart'):
            if 'cart-update' in request.POST:
                cart[request.POST.get('cart-update')][request.POST.get('size')] = int(request.POST.get('quantity'))
                request.session.modified = True
                updated = True
            elif 'cart-remove' in request.POST:
                product = cart[request.POST.get('cart-remove')]
                del product[request.POST.get('size')]
                if not product:
                    del cart[request.POST.get('cart-remove')]
                request.session.modified = True
                updated = True


def details(request):
    """
    Get products, individual prices, total cart price and quantity.

    Set values as details keys so total can be accessed from the checkout view 
    """

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
    details.cart_items = cart_items
    details.prices = prices
    details.total = total
    details.quantity = quantity


def cart_items(request):
    """Add cart items and details to context"""

    global updated
    if updated == False:
        product_update(request)

    details(request)

    context = {
        'cart_items': details.cart_items,
        'prices': details.prices,
        'total': details.total,
        'quantity': details.quantity,
        'updated': updated
    }

    updated = False

    return context
