from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect('rollpaper:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('rollpaper:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():

            user = form.get_user()
            auth_login(request, user)

            next_url = request.GET.get('next')

            return redirect(next_url or 'rollpaper:index')

    else:
        form = AuthenticationForm()

    context = {
        'form':form,
    }
        
    return render(request, 'accounts/login.html', context)


@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('rollpaper:index')


@login_required
def update(request):

    if request.method == 'POST':
        form1 = CustomUserChangeForm(request.POST, instance=request.user)
        form2 = PasswordChangeForm(request.user, request.POST)
        if form1.is_valid():
            if (not request.POST.get('password') 
                and not request.POST.get('new_password1') 
                and not request.POST.get('new_password2')):
                form1.save()
            else:
                form1.save()
                form2.save()

                update_session_auth_hash(request, form2.user)

            return redirect('rollpaper:index')

    form1 = CustomUserChangeForm(instance = request.user) # 현재 로그인 된 유저 객체
    form2 = PasswordChangeForm(user=request.user)
    context = {
        'form1' : form1,
        'form2' : form2
    }
    return render(request, 'accounts/update.html', context)


# adminpass


# @login_required
# def change_password(request):

#     if request.method == 'POST':
#         # 1) 현재 로그인된 사용자 정보 바인딩 (request.user)
#         # 2) 사용자가 보낸 수정된 비밀번호 정보 (request.POST)
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()

#             update_session_auth_hash(request, form.user) # form에서 가져온 user (request.user 그대로 쓰면 안됨)
#             return redirect('posts:index')
#     else:
#         form = PasswordChangeForm(user=request.user)

#     context = {
#         'form' : form,
#     }

#     return render(request, 'accounts/change_password.html', context)
