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

