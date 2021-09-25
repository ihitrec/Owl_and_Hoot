from django.shortcuts import render
from .models import Order
from products.models import Product
from .forms import OrderForm


def checkout(request):

    # Return to home if cart empty
    if 'cart-remove' in request.POST and len(request.session['cart']) == 1 or not request.session['cart']:
        return render(request, 'home/index.html')
    
    if 'postcode' in request.POST:
        cart = request.session['cart']
        items={}
        for product_id in list(cart.keys()):
            items[Product.objects.get(id=product_id).name] = cart[product_id]
        order = Order.objects.create(
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
        'form':OrderForm(),
        'stripe_public_key': 'pk_test_51JddLyAj5ldMa6pFqrs5yfLT0Z15WENJT2DydLYwBWRCRkpcEmLhZdiy01pn1FSd6zpEU6WObWFuirXiAe3XvBJy00XE6tWNrN',
        'client_secret':'test client secret'
    }    

    return render(request, 'checkout/checkout.html', context)