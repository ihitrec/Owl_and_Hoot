# pylint: disable=no-member
from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Q


def categories(request, category):
    brand = []
    if category in ['all', 'puma', 'nike', 'adidas']:
        if 'search' in request.GET:

            # Add lowercase search words to query list
            search = request.GET['search']
            query = [x.lower() for x in search.split()]

            # Set brand filter if brand in query, remove brands from query
            for word in query:
                if word in ('nike', 'puma', 'adidas'):
                    brand.append(word)
            query = list(set(query) - set(['nike', 'puma', 'adidas']))

            # Filter products by gender if phrase or synonym in query
            if (not set(['male', 'men', 'boy', 'man']).isdisjoint(query)):
                products = Product.objects.filter(gender='male')
            elif (not set(
                    ['female', 'women', 'girl', 'woman']).isdisjoint(query)):
                products = Product.objects.filter(gender='female')
            else:
                products = Product.objects.all()

            # Extend query with synonyms for matched words
            synonyms = [
                ['runner', 'runners', 'footwear', 'sneaker', 'sneakers',
                 'shoe', 'shoes'],
                ['shirt', 'tee', 't-shirt', 'tshirt'],
                ['jeans', 'trousers', 'pants', 'denim']]
            for values in synonyms:
                if (not set(values).isdisjoint(query)):
                    query.extend(values)

            # If product name or category is in filter, add to results
            filter = Q()
            for word in query:
                filter |= Q(name__icontains=word)
                filter |= Q(category__icontains=word)
            products = products.filter(filter)
        else:
            products = Product.objects.all()
    elif category == 'female':
        products = Product.objects.filter(gender='female')
    elif category == 'male':
        products = Product.objects.filter(gender='male')
    elif category == 'sale':
        products = Product.objects.exclude(sale_price__isnull=True)
    return render(request, 'products/categories.html', {
        'products': products, 'brand': brand})


def product(request, product):
    try:
        product = Product.objects.get(id=product)
        return render(request, 'products/product.html', {'product': product})
    except Product.DoesNotExist:
        return redirect('home')
