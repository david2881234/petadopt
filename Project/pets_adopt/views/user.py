#coding:utf-8
from django.contrib.auth import login, authenticate
from django.contrib import messages,auth
from pets_adopt.forms import UserForm,LoginForm
from django.shortcuts import render,redirect,get_object_or_404

def user_signup(request):
    template_name = 'pets_adopt/signup.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = request.POST['username']
            password = form.clean_password2()
            form.save()
            user = authenticate(username = user_name, password = password)
            if user.is_active:
                login(request,user)
            return redirect('index')
    else:
        form = UserForm
    return render(request,template_name,{'form': form})

def user_login(request):
    template_name = 'pets_adopt/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user_name = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = user_name,password = password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
    else:
        form = LoginForm()
        return render(request,template_name,{'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect('index')
