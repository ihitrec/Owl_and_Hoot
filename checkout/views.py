from django.shortcuts import render


def checkout(request):

    # Redirect to home if last item removed from cart
    if 'cart-remove' in request.POST and len(request.session['cart']) == 1:
        return render(request, 'home/index.html')

    return render(request, 'checkout/checkout.html')