# coding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from models import Pets


class UserForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        name = forms.CharField(label='姓名',max_length=50,required=True)
        fields = ('username','name','email', 'gender', 'state','profile')
        labels = {
            'username': '帳號',
            'email': 'E-mail',
            'gender': '性別',
            'state': '狀態',
            'profile': '個人自述',
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='帳號',max_length=255, required=True)
    password = forms.CharField(label='密碼',widget=forms.PasswordInput, required=True)

class Post_Pet(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ('pet_name','content')
        labels = {
            'pet_name':'寵物的名字',
            'content':'寵物介紹一下',
        }