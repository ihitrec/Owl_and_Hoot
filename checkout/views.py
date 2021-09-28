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

    if 'postcode' in request.POST:
        cart = request.session['cart']

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
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
                total_cost=details.total
            )
            return redirect('home')
    else:
        order_form = OrderForm()
        total = details.total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    context = {
        'form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
