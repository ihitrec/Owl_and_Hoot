from django.shortcuts import render
from .models import Product


def categories(request, category):
    products = Product.objects.all()
    return render(request, 'products/categories.html', {'products': products})
