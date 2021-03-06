#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


class NewUser(AbstractUser):  # (username,email,password1,password2)
    sex_choice = (
        ('m', u'男'),
        ('f', u'女'),
    )

    name = models.CharField(u'姓名', max_length=20, default='')
    gender = models.CharField(u'性別', max_length=1,  choices=sex_choice, default='m')
    id_card_num = models.CharField(u'身份證字號', max_length=10, default='')
    mobile = models.CharField(u'手機號碼', max_length=10, default='')
    home_tel = models.CharField(u'家電', max_length=11, default='')
    address = models.CharField(u'地址', max_length=50, default='')
    facebook = models.CharField(u'Facebook', max_length=100, default='')
    line = models.CharField(u'Line', max_length=20, default='')
    profile = models.TextField(u'個人自述', max_length=200, default='')
    photo = models.ImageField(u'身份證照片',upload_to='person',null=True)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    credit = (
        (0, u'優良'),
        (1, u'普通'),
        (2, u'不良'),
    )
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField(u'評語')
    credit = models.IntegerField(u'信用', choices=credit, default=0)

    def __unicode__(self):
        return self.comment

class Pets(models.Model):
    pet_status_choice = (
        (0, u'待認養'),
        (1, u'已領養'),
    )
    chip_choice = (
        (True, u'有'),
        (False, u'無'),
    )
    neuter_choice = (
        (True, u'有'),
        (False, u'無'),
    )
    dog_or_cat_choice = (
        (0, u'狗'),
        (1, u'貓'),
    )
    sex_choice = (
        (True,u'男生'),
        (False,u'女生'),
    )
    area_choice = (
        (0, u'台北市'),
        (1, u'新北市'),
        (2, u'桃園市'),
        (3, u'新竹縣'),
        (4, u'新竹市'),
        (5, u'苗栗縣'),
        (6, u'台中市'),
        (7, u'彰化縣'),
        (8, u'南投縣'),
        (9, u'雲林縣'),
        (10, u"嘉義縣"),
        (11, u'嘉義市'),
        (12, u'台南市'),
        (13, u'高雄市'),
        (14, u'屏東縣'),
        (15, u'台東縣'),
        (16, u'花蓮縣'),
        (17, u'宜蘭縣'),

    )
    size_choice = (
        (0,u'小型'),
        (1,u'中型'),
        (2,u'大型'),
    )
    age_choice = (
        (0,u'幼年'),
        (1,u'成年'),
    )
    color_choice = (
        (0,u'白色'),
        (1,u'黑色'),
        (2,u'棕色'),
        (3,u'黃色'),
        (4,u'花色'),
        (5,u'虎班'),
        (6,u'其他')
    )
    pet_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='current_owner',default='')
    pet_publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='previous_owner',default='')
    pet_name = models.CharField(u'寵物名', max_length=30, default='')
    state = models.IntegerField(u'領養狀態', choices=pet_status_choice, default=0)
    content = models.TextField(u'寵物簡介')
    color = models.IntegerField(u'毛色', choices=color_choice, default=0)
    chip = models.BooleanField(u'晶片有無', choices=chip_choice, default=False)
    neuter = models.BooleanField(u'是否有結紮', choices=neuter_choice, default=False)
    dog_or_cat = models.IntegerField(u'狗或貓', choices=dog_or_cat_choice, default=0)
    area = models.IntegerField(u'寵物所在地區', choices=area_choice, default=0)
    breed = models.CharField(u'品種', max_length=20, default='')
    age = models.IntegerField(u'年紀', choices=age_choice, default=0)
    sex = models.BooleanField(u'寵物性別',choices=sex_choice,default=True)
    size = models.IntegerField(u'體型',choices=size_choice,default=0)
    photo = models.ImageField(upload_to='pet', null=True)

    def __unicode__(self):
        return self.pet_name


class Adopt(models.Model):
    mode = (
        (0, u'待批准'),
        (1, u'通過'),
        (2, u'拒絕'),
        (3, u'待領養者確認'),
        (4, u'待送養者確認'),
    )
    adopt_person = models.ForeignKey(settings.AUTH_USER_MODEL)
    adopt_pet = models.ForeignKey(Pets)
    mode = models.IntegerField(u'審核狀態', choices=mode, default=0)
    content = models.TextField(u'認養理由')

    def __unicode__(self):
        return unicode(self.adopt_person)


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    pet = models.ForeignKey(Pets)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='article',null=True)

    def __unicode__(self):
        return self.title


"""
class visit_msg(models.Model):
    mode = (
        (0,u'待批准'),
        (1,u'通過'),
        (2,u'拒'),
    )
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL)
    visit_pet = models.ForeignKey(Pets)
    content = models.TextField(u'給主人的話')
    visit_date = models.DateTimeField(u'探訪時間')
"""
