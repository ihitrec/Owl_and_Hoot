from django.shortcuts import render
from .models import Product


def categories(request, category):
    products = Product.objects.all()
    return render(request, 'products/categories.html', {'products': products})


def product(request, product):
    product = Product.objects.get(id=product)
    return render(request, 'products/product.html', {'product': product})
