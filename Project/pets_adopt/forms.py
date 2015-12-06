# coding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from models import Pets,Adopt,Blog,Comment
from django.utils.safestring import mark_safe

class HorizRadioRenderer(forms.RadioSelect.renderer): #自訂radio選項redner樣式
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class UserForm(UserCreationForm):
    name = forms.CharField(label='姓名',max_length=20,required=True)
    facebook = forms.CharField(label='Facebook網址',max_length=100,required=True)
    address = forms.CharField(label='地址',max_length=50,required=True)
    mobile = forms.CharField(label='手機號碼',max_length=10,required=True)
    id_card_num = forms.CharField(label='身份證字號',max_length=10,required=True)
    line = forms.CharField(label='Line ID(非必填)',max_length=20,required=False)
    home_tel = forms.CharField(label='家電(非必填)',max_length=10,required=False)
    photo = forms.ImageField(label='身份證照')
    class Meta:
        model = get_user_model()
        fields = ('username','name','gender','email','id_card_num','address','mobile','home_tel','facebook','line','profile','photo')
        labels = {
            'username': '帳號',
            'email': 'E-mail',
            'gender': '性別',
            'profile': '個人自述',
        }

class User_Edit(forms.ModelForm):
    line = forms.CharField(label='Line ID(非必填)',max_length=20,required=False)
    home_tel = forms.CharField(label='家電(非必填)',max_length=10,required=False)
    class Meta():
        model = get_user_model()
        fields = ('email','profile','mobile','home_tel','facebook','line','profile')

'''class Change_User_State(forms.ModelForm):
    class Meta():
        model = get_user_model()
        fields = ('state',)
'''

class LoginForm(forms.Form):
    username = forms.CharField(label='帳號',max_length=255, required=True)
    password = forms.CharField(label='密碼',widget=forms.PasswordInput, required=True)

class Post_Pet(forms.ModelForm):
    photo = forms.ImageField(label='放張寵物照')
    breed = forms.CharField(label='品種(非必填)',max_length=10,required=False)
    class Meta:
        model = Pets
        fields = ('dog_or_cat','pet_name','sex','age','size','color','breed','area','chip','neuter','content','photo')
        labels = {
            'dog_or_cat':'狗或貓',
            'pet_name':'寵物的名字',
            'sex':'寵物性別',
            'age':'年紀',
            'size':'體型',
            'color':'毛色',
            'area':'地區',
            'chip':'晶片有無',
            'neuter':'有無結紮',
            'content':'寵物介紹一下',
        }
        widgets = {
            'dog_or_cat': forms.RadioSelect(renderer=HorizRadioRenderer),
            'chip': forms.RadioSelect(renderer=HorizRadioRenderer),
            'neuter': forms.RadioSelect(renderer=HorizRadioRenderer),
        }


class Adopt_Request_Form(forms.ModelForm):
    class Meta:
        model = Adopt
        fields = ('content',)


class Blog_Post(forms.ModelForm):
    photo = forms.ImageField(label='上傳照片')
    class Meta:
        model = Blog
        fields = ('title','content','photo')
        labels = {
            'title':'標題',
            'content':'內容',
        }


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('credit','comment',)
        labels = {
            'credit':'給送養者評價',
            'comment':'寫下你對對方的評語',
        }
        widgets = {
            'credit': forms.RadioSelect(renderer=HorizRadioRenderer)
        }