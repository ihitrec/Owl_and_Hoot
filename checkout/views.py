# pylint: disable=no-member
from django.shortcuts import render, redirect
from django.conf import settings

from .models import Order
from products.models import Product
from .forms import OrderForm
from cart.contexts import product_update, details

import stripe


def checkout(request):

    product_update(request)
    details(request)

    # Return to home if cart empty
    if not request.session['cart']:
        return redirect('home')

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    total = details.total
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if 'postcode' in request.POST:
        cart = request.session['cart']
        items = {}
        for product_id in list(cart.keys()):
            items[Product.objects.get(id=product_id).name] = cart[product_id]
        Order.objects.create(
            products=items,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            country=request.POST.get('country'),
            postcode=request.POST.get('postcode'),
            city=request.POST.get('city'),
            street_address1=request.POST.get('street_address1'),
            street_address2=request.POST.get('street_address2'),
            total_cost=request.POST.get('total_cost')
            )

    context = {
        'form': OrderForm(),
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
