from django.shortcuts import redirect


def add_to_cart(request, product_id):
    """Save added product, quantity and size to session"""

    quantity = int(request.POST.get('num-of-products'))
    cart = request.session.get('cart', {})
    size = request.POST.get('size')

    if product_id in list(cart.keys()):
        if size in list(cart[product_id].keys()):
            cart[product_id][size] += quantity
        else:
            cart[product_id][size] = quantity
    else:
        cart[product_id] = {size: quantity}

    request.session['cart'] = cart
    return redirect('product', product=product_id)
