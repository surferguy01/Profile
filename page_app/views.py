from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import*
from .forms import ContactForm

import bcrypt


def index(request):
    return render(request, 'index.html')



def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            
            html = render_to_string('contact_form.html', {
                'name' : name,
                'sender' : sender,
                'subject' : subject,
                'message' : message
            })

            send_mail(subject, message, 'noreply@anthonyives.com', ['anthonyives01@gmail.com'], html_message=html)

            return redirect ('/submission')
 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def work(request):
    return render(request, 'work.html')


def about(request):
    return render(request, 'about.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')

def submission(request):
    return render(request, 'submission.html')