from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Product
from cart.contexts import cart_contents

import stripe 



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLISHABLE
    stripe_secret_key = settings.STRIPE_SECRET
  
    
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment!")
        return redirect(reverse('products'))
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm()    
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret' : intent.client_secret,
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
                        