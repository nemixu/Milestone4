from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from products.models import Product, Category



def search_view(request):
    """
    View to handle search post requests submitted by user
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria! here is some products")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.info(request, "Sorry we couldn't match your search!")
                return redirect(reverse('products'))

    context = {
        'products' : products,
        'search_term' : query,
    }

    return render(request, 'products/products.html', context)
