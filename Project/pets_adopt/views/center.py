#coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.models import Pets,Adopt,NewUser

@login_required
def main(request,user_id): #會員中心，可修改個人資料及寵物資料，以及觀看送領養紀錄
    user = get_object_or_404(NewUser, id=user_id)
    template_name = "pets_adopt/member_center/main.html"
    return render(request,template_name,{'user': user,'nbar':'memcenter'})


@login_required
def my_pet(request, user_id): #屬於我的寵物
    template_name = "pets_adopt/member_center/my_pet.html"
    user = get_object_or_404(NewUser, id=user_id)
    pet = Pets.objects.filter(pet_owner=user)
    return render(request, template_name, {'user':user,'pet':pet,'nbar':'memcenter'})

# Adopt.mode=0:待批準,1:通過,2:拒絕,3:待領養者確認,4:待送養者確認
@login_required
def sending_pet(request, user_id): #送養中的寵物
    template_name = "pets_adopt/member_center/sending_pet.html"
    user = get_object_or_404(NewUser, id=user_id)
    pet = Pets.objects.filter(pet_publisher=user, state=0)
    return render(request, template_name, {'user':user,'pet':pet,'nbar':'memcenter'})

@login_required
def receiving_pet(request, user_id): #想領養的寵物
    template_name = "pets_adopt/member_center/receiving_pet.html"
    user = get_object_or_404(NewUser, id=user_id)
    adopts = Adopt.objects.filter(adopt_person=user) #這個人的所有領養單
    return render(request, template_name, {'user':user,'adopt':adopts,'nbar':'memcenter'})