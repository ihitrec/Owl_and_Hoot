from django.shortcuts import render


def checkout(request):

    # Return to home if cart empty
    if 'cart-remove' in request.POST and len(request.session['cart']) == 1 or not request.session['cart']:
        return render(request, 'home/index.html')

    return render(request, 'checkout/checkout.html')