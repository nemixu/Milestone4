from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail

from .forms import Contact


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
        form = Contact(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect(reverse('contact_success'))
            # send_mail(
            #     'Contact from website' + message_name,
            #     message,
            #     message_email,
            #     ['test@test.com'],
            # )
        else:
            messages.error(request,
                           'Sorry something went wrong, please ensure all fields are correctly filled out')
    else:
        form = Contact()

    template = 'home/contact.html'
    context = {
        'page_title': page_title,
        'send_mail' : send_mail,
        'form':form,
    }

    return render(request, template, context)


def contact_success(request):
    """
    contact_success to return the template,
    page title and context of the view.
    """
    page_title = "Thanks for contacting"
    template = "home/contact_success.html"

    context = {
        'page_title' : page_title
    }

    return render(request, template, context)
