from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()[:4]
    return render(request, 'home.html', {'projects': projects})

def projectcard(request):
    projects = Project.objects.all()
    return render(request, 'projectcard.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')
