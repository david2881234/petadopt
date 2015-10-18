#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class NewUser(AbstractUser):
    sex_choice = (
        ('f',u'女'),
        ('m',u'男')
    )
    adopt_status = (
        (1,u'送養者'),
        (2,u'領養者'),
        (3,u'志工')
    )
    name = models.CharField(u'姓名',max_length=20)
    gender = models.CharField(u'性別', max_length=1, choices=sex_choice, default='f')
    state = models.IntegerField(u'狀態', choices=adopt_status, default=1)
    profile = models.TextField(u'個人自述')

    def __unicode__(self):
        return self.name


class Pets(models.Model):
    pet_status = (
        (0,u'待認養'),
        (1,u'已領養'),
    )
    pet_publisher = models.ForeignKey(settings.AUTH_USER_MODEL)
    pet_name = models.CharField(u'寵物名',max_length=30)
    state = models.IntegerField(u'領養狀態',choices=pet_status,default=0)
    content = models.TextField(u'寵物簡介')

