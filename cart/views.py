from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.

def cart(request):
    """A view to return the cart page"""
    
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add an item or quantitity of items to the cart"""
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))    
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.info(request, f'Updated { product.name } quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added { product.name } to your cart')
        
    request.session['cart'] = cart   
    return redirect(redirect_url)


def update_cart(request, item_id):
    """update the cart quantity"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=item_id)
    if quantity > 0:
        cart[item_id] = quantity
        messages.info(request, f'Updated { product.name } quantity in your cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed { product.name } from your cart')
    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """remove an item from the cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.success(request, f'Removed { product.name } from your cart')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)