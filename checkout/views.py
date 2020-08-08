from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from cart.contexts import cart_contents


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()    
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
    }    
    
    return render(request, template, context)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    form_data = {
        'full_name' : request.POST['full_name'],
        'email' : request.POST['email'],
        'phone_number' : request.POST['phone_number'],        
    }
    order_form = OrderForm(form_data)
    if order_form.is_valid():
        order = order_form.save()
        for item_id, item_data in cart.items():
            try:
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()    
            except Product.DoesNotExist:
                messages.error(request, (
                    "One of the products in your cart wasn't found in our database."
                    "please call us for assistance!")
                )
                order.delete()
                return redirect(reverse('cart'))
                        