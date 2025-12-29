from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings 

def home(request):
    return render(request, 'home.html')

def projectcard(request):
    return render(request, 'projectcard.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        request_type = request.POST.get('request')
        message = request.POST.get('message')

        subject = f"New {request_type} inquiry from {name}"
        full_message = (
            f"You received a new contact form submission:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Request Type: {request_type}\n\n"
            f"Message:\n{message}"
        )

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,          
            ['balkrishna28tiwari@gmail.com'],   
            fail_silently=False,
        )

        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('contact')

    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')