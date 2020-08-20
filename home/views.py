from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

def index(request):
    """ View to return the index page """
    page_title = "Home Page"
    template = "home/index.html"
    context = {
        'page_title': page_title,
    }
    return render(request, template, context)


def about(request):
    """Returns the about page"""
    page_title = "About us"
    template = 'home/about.html'
    context = {
        'page_title': page_title,
    }
    return render(request, template, context)

def contact(request):
    """View to handle the contact page"""
    page_title = "Contact Us"
    
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            'Contact from website' + message_name,
            message,
            message_email,
            ['test@test.com],
        )
    
    
    template = 'home/contact.html'
    context = {
        'page_title': page_title,
        'send_mail' : send_mail,
    }
    
    return render(request, template, context)