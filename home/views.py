from django.shortcuts import render

# Create your views here.

def index(request):
    """ View to return the index page """
    page_title = "Home Page"
    return render(request, 'home/index.html', {'page_title': page_title})


def about(request):
    """Returns the about page"""
    page_title = "About us"
    return render(request, 'home/about.html', {'page_title': page_title})