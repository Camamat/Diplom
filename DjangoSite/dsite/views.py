from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def login(request):
    return render(request, 'base.html')

def register(request):
    return render(request, 'registration_page.html')
