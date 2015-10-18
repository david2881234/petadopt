#coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import UserForm,LoginForm,Post_Pet
from django.contrib import messages,auth
from models import Pets

def index(request):
    template_name = 'pets_adopt/index.html'
    return render(request,template_name,{})
def user_signup(request):
    template_name = 'pets_adopt/signup.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = request.POST['username']
            password = form.clean_password2()
            state = request.POST['state']
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


@login_required
def pet_new(request):
    template_name = 'pets_adopt/writing.html'
    if request.method == 'POST':
        form = Post_Pet(request.POST)
        if form.is_valid:
            Pets = form.save(commit=False)
            Pets.pet_publisher = request.user
            Pets.save()
            return redirect('pet_detail',pets_id=Pets.id)
    else:
        form = Post_Pet()
        return render(request,template_name,{'form':form})


def pet_detail(request, pets_id):
    template_name = 'pets_adopt/pets_detail.html'
    pet = get_object_or_404(Pets, id=pets_id)
    return render(request,template_name,{'pet':pet})

# Create your views here.
