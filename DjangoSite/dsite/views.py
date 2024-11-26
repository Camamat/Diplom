from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import UserRegisterForm
from django.http import HttpResponse

def login(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            login_ = form.cleaned_data['login_']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            return render(request, 'user.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'registration_page.html', {'form': form})

def page(request):
    user = Users.objects.all()
    context = {
        'user':user,
    }
    return render(request, 'user.html', context)
