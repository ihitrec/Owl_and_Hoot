from django.shortcuts import render
from .models import Product


def categories(request, category):
    if category in ['all', 'puma', 'nike', 'adidas']:
        products = Product.objects.all()
    elif category == 'female':
        products = Product.objects.filter(gender='female')
    elif category == 'male':
        products = Product.objects.filter(gender='male')
    elif category == 'sale':
        products = Product.objects.exclude(sale_price__isnull=True)
    return render(request, 'products/categories.html', {'products': products})


def product(request, product):
    product = Product.objects.get(id=product)
    return render(request, 'products/product.html', {'product': product})
