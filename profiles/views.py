from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile, Diary
from .forms import UserProfileForm, DiaryEntry

from checkout.models import Order

# Create your views here.
def profile(request):
    """View to display the users profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        
    orders = profile.orders.all()
    
    form = UserProfileForm(instance=profile)
    template ='profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, template, context)



def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }
    
    return render(request, template, context)

def diary(request):
    diaries = Diary.objects.order_by('-date_posted')
    context = {
        'diaries': diaries
        }
    
    return render(request, context)
    
    
    
def diary_entry(request):
    if request.method == 'POST':
        form = DiaryEntry(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diary entry has been updated successfully')
            return redirect('profile')
        else:
            form = DiaryEntry()
        context = {
            'form': form
        }
        
        return render(request, context)    