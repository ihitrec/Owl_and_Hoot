# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .models import Order
from products.models import Product
from .forms import OrderForm
from cart.contexts import product_update, details

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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
                items[Product.objects.get(
                    id=product_id).name] = cart[product_id]
            saved_order = Order.objects.create(
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
            return redirect(reverse('checkout_success', args=[saved_order.pk]))
        else:
            messages.error(request, 'There was an error with your form.')
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


def checkout_success(request, order_number):
    order = Order.objects.get(id=order_number)

    if 'cart' in request.session:
        request.session['cart'] = {}

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
