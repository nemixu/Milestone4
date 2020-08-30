from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

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


def contact(request):
    """View to handle the contact page"""
    page_title = "Contact Us"
    admin_email = settings.ADMIN_EMAIL
    subject = render_to_string(
        'emails/contact_request_subject.txt'
    )
    if request.method == "POST":
        form = Contact(request.POST)

        if form.is_valid():
            message = request.POST.get('message', '')
            reply_email = request.POST.get('email', '')
            subject = render_to_string('emails/contact_request_subject.txt')
            email = EmailMessage(
                subject,
                message,
                to=["s.r.seagrave@gmail.com"],
                headers={"Reply-to": reply_email},
            )
            form.save()
            try:
                email.send()
                messages.success(request, 'Your message has been sent successfully')
            except Exception as e:
                messages.error(request, f"Message not sent,Error! {e}")
            return redirect(reverse('contact_success'))
        else:
            messages.error(request,
                           'Sorry something went wrong, please ensure all fields are correctly filled out')
    else:
        form = Contact()

    template = 'home/contact.html'
    context = {
        'page_title': page_title,
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
