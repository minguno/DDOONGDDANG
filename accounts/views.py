from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import (
    authenticate, 
    login as auth_login,
    logout as auth_logout,

)

from accounts.forms import CustomCreationForm
from .models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
)

# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect('roll_paper:main')
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = CustomCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
   

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('roll_paper:main') #메인 페이지로 이동
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
