from django.shortcuts import render


def categories(request, category):
    return render(request, 'products/categories.html')
