#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class NewUser(AbstractUser): #(username,email,password1,password2)
    sex_choice = (
        ('m',u'男'),
        ('f',u'女'),
    )
    adopt_status = (
        (1,u'送養者'),
        (2,u'領養者'),
        (3,u'志工')
    )
    name = models.CharField(u'姓名',max_length=20)
    gender = models.CharField(u'性別', max_length=1, choices=sex_choice, default='m')
    state = models.IntegerField(u'狀態', choices=adopt_status, default=1)
    profile = models.TextField(u'個人自述')
    id_card_num = models.CharField(u'身份證字號',max_length=10)
    mobile = models.CharField(u'手機號碼',max_length=10)
    home_tel = models.CharField(u'家電',null=True)
    address = models.CharField(u'地址')
    def __unicode__(self):
        return self.name


class Pets(models.Model):
    pet_status = (
        (0,u'待認養'),
        (1,u'已領養'),
    )
    chip = (
        (True,u'有'),
        (False,u'無'),
    )
    dog_or_cat = (
        (0,u'狗'),
        (1,u'貓'),
    )
    area = (
        (0,u'台北市'),
        (1,u'新北市'),
        (2,u'桃園市'),
        (3,u'新竹縣'),
        (4,u'新竹市'),
        (5,u'苗栗縣'),
        (6,u'台中市'),
        (7,u'彰化縣'),
        (8,u'南投縣'),
        (9,u'雲林縣'),
        (10,u"嘉義縣"),
        (11,u'嘉義市'),
        (12,u'台南市'),
        (13,u'高雄市'),
        (14,u'屏東縣'),
        (15,u'台東縣'),
        (16,u'花蓮縣'),
        (17,u'宜蘭縣'),

    )
    reserve_visit = (
        (True,u'有'),
        (False,u'無'),
    )
    pet_publisher = models.ForeignKey(settings.AUTH_USER_MODEL)
    pet_name = models.CharField(u'寵物名',max_length=30)
    state = models.IntegerField(u'領養狀態',choices=pet_status,default=0)
    content = models.TextField(u'寵物簡介')
    color = models.CharField(u'毛色')
    chip = models.BooleanField(u'晶片有無',choice = chip,Default = False)
    dog_or_cat = models.CharField(u'狗或貓',choice = dog_or_cat,default = 0)
    area = models.CharField(u'寵物所在地區',choice = area,default = 0)
    breed = models.CharField(u'品種')
    reserve_visit = models.BooleanField(u'預約探訪',choice = reserve_visit,default = False)


    def __unicode__(self):
        return self.pet_name


class Adopt(models.Model):
    mode = (
        (0,u'待批准'),
        (1,u'通過'),
        (2,u'拒絕'),
    )
    adopt_person = models.ForeignKey(settings.AUTH_USER_MODEL)
    adopt_pet = models.ForeignKey(Pets)
    mode = models.IntegerField(u'審核',choices=mode,default=0)
    content = models.TextField(u'認養理由')

    def __unicode__(self):
        return unicode(self.adopt_person)


class visit_msg(models.Model):
    mode = (
        (0,u'待批准'),
        (1,u'通過'),
        (2,u'拒絕'),
    )
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL)
    visit_pet = models.ForeignKey(Pets)
    content = models.TextField(u'給主人的話')
    visit_date = models.DateTimeField(u'探訪時間')


class pet_photo(models.Model):
    pet = models.ForeignKey(Pets)
    image_file = models.FileField(upload_to='media/pet_image')

