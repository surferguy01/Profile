from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import*
from .forms import ContactForm

import bcrypt


def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # subject = request.POST['subject']
        message = request.POST['message']

        # send_mail(
            # first_name, # subject (need to change first_name to subject option later)
            # message, # message
            # email, # from email
            # ['anthony.ives01@gmail.com']# to email

        # )
        return render(request, 'contact.html', {'first_name': first_name})


    else: 
        return render(request, 'contact.html')

def work(request):
    return render(request, 'work.html')

def about(request):
    return render(request, 'about.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')