#coding:utf-8
from django.contrib.auth import login, authenticate
from django.contrib import messages,auth
from pets_adopt.forms import UserForm,User_Edit
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.models import NewUser,Adopt,Pets,Comment


def user_signup(request):
    template_name = 'pets_adopt/signup.html'
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            image_file = request.FILES["photo"]
            user_name = request.POST['username']
            password = form.clean_password2()
            form.save(commit=False)
            form.photo = image_file
            form.save()
            user = authenticate(username = user_name, password = password)
            if user.is_active:
                login(request,user)
                messages.success(request,u'註冊成功並登錄')
            return redirect('index')
    else:
        form = UserForm
    return render(request,template_name,{'form': form,'nbar':'signup'})

@login_required
def user_edit(request,user_id): #要尋找更好寫法
    user = get_object_or_404(NewUser, id=user_id)
    template_name = "pets_adopt/user_edit.html"
    if request.method =='POST':
        form = User_Edit(request.POST, instance=user)
        form.save()
        messages.success(request,u'修改成功')
        return redirect('index')
    else:
        form = User_Edit(instance = user)
        return render(request,template_name,{'form':form,'user':user})


def user_detail(request,user_id):
    usr = get_object_or_404(NewUser, id=user_id)
    template_name = "pets_adopt/user_detail.html"
    all_comment = Comment.objects.filter(person = usr)
    all_pet = Pets.objects.filter(pet_owner=usr)
    good = 0
    ok = 0
    bad = 0
    for cmt in all_comment: #顯示這個人的評價
        if cmt.credit == 0:
            good += 1
        elif cmt.credit == 1:
            ok += 1
        elif cmt.credit == 2:
            bad += 1
    return render(request,template_name, {'usr':usr,'all_comment':all_comment,'good':good,'ok':ok,'bad':bad,'all_pet':all_pet})




"""
def user_login(request):
    template_name = 'pets_adopt/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user_name = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = user_name,password = password)
            if user is not None and user.is_active:
                login(request, user)
                    return redirect('index')

    else:
        form = LoginForm()
        return render(request,template_name,{'form': form})
"""

"""

def user_logout(request):
    auth.logout(request)
    return redirect('index')
"""
