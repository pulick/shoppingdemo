from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def SearchResult(request):
    product = None
    query = None
    if 'q' in request.GET:  # Fix the typo here: "request.Get" should be "request.GET"
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
