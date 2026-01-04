from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings 
import resend

def home(request):
    return render(request, 'home.html')

def projectcard(request):
    return render(request, 'projectcard.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        request_type = request.POST.get("request")
        message = request.POST.get("message")

        subject = f"New {request_type} inquiry from {name}"

        full_message = f"""
New contact form submission:

Name: {name}
Email: {email}
Request Type: {request_type}

Message:
{message}
        """

        try:
            resend.api_key = settings.RESEND_API_KEY

            resend.Emails.send({
                "from": "Portfolio Contact <onboarding@resend.dev>",
                "to": ["krishna40tiwari@gmail.com"],
                "subject": subject,
                "text": full_message,
            })

            messages.success(request, "Thank you! Your message has been sent.")
        except Exception as e:
            print("Resend error:", e)
            messages.error(request, "Something went wrong. Please try again later.")

        return redirect("contact")

    return render(request, "contact.html")

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def about(request):
    return render(request, 'about.html')