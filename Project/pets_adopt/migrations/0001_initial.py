# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default=b'', max_length=20, verbose_name='\u59d3\u540d')),
                ('gender', models.CharField(default=b'm', max_length=1, verbose_name='\u6027\u5225', choices=[(b'm', '\u7537'), (b'f', '\u5973')])),
                ('id_card_num', models.CharField(default=b'', max_length=10, verbose_name='\u8eab\u4efd\u8b49\u5b57\u865f')),
                ('mobile', models.CharField(default=b'', max_length=10, verbose_name='\u624b\u6a5f\u865f\u78bc')),
                ('home_tel', models.CharField(default=b'', max_length=11, verbose_name='\u5bb6\u96fb')),
                ('address', models.CharField(default=b'', max_length=50, verbose_name='\u5730\u5740')),
                ('facebook', models.CharField(default=b'', max_length=20, verbose_name='Facebook')),
                ('line', models.CharField(default=b'', max_length=20, verbose_name='Line')),
                ('profile', models.TextField(default=b'', max_length=200, verbose_name='\u500b\u4eba\u81ea\u8ff0')),
                ('photo', models.ImageField(upload_to=b'person', null=True, verbose_name='\u7167\u7247')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.IntegerField(default=0, verbose_name='\u5be9\u6838', choices=[(0, '\u5f85\u6279\u51c6'), (1, '\u901a\u904e'), (2, '\u62d2\u7d55'), (3, '\u5f85\u9818\u990a\u8005\u78ba\u8a8d'), (4, '\u5f85\u9001\u990a\u8005\u78ba\u8a8d')])),
                ('content', models.TextField(verbose_name='\u8a8d\u990a\u7406\u7531')),
                ('adopt_person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'article')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='\u8a55\u8a9e')),
                ('credit', models.IntegerField(default=0, verbose_name='\u4fe1\u7528', choices=[(0, '\u512a\u826f'), (1, '\u666e\u901a'), (2, '\u4e0d\u826f')])),
                ('person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_name', models.CharField(default=b'', max_length=30, verbose_name='\u5bf5\u7269\u540d')),
                ('state', models.IntegerField(default=0, verbose_name='\u9818\u990a\u72c0\u614b', choices=[(0, '\u5f85\u8a8d\u990a'), (1, '\u5df2\u9818\u990a')])),
                ('content', models.TextField(verbose_name='\u5bf5\u7269\u7c21\u4ecb')),
                ('color', models.CharField(default=b'', max_length=5, verbose_name='\u6bdb\u8272')),
                ('chip', models.BooleanField(default=False, verbose_name='\u6676\u7247\u6709\u7121', choices=[(True, '\u6709'), (False, '\u7121')])),
                ('neuter', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6709\u7d50\u7d2e', choices=[(True, '\u6709'), (False, '\u7121')])),
                ('dog_or_cat', models.IntegerField(default=0, verbose_name='\u72d7\u6216\u8c93', choices=[(0, '\u72d7'), (1, '\u8c93')])),
                ('area', models.IntegerField(default=0, verbose_name='\u5bf5\u7269\u6240\u5728\u5730\u5340', choices=[(0, '\u53f0\u5317\u5e02'), (1, '\u65b0\u5317\u5e02'), (2, '\u6843\u5712\u5e02'), (3, '\u65b0\u7af9\u7e23'), (4, '\u65b0\u7af9\u5e02'), (5, '\u82d7\u6817\u7e23'), (6, '\u53f0\u4e2d\u5e02'), (7, '\u5f70\u5316\u7e23'), (8, '\u5357\u6295\u7e23'), (9, '\u96f2\u6797\u7e23'), (10, '\u5609\u7fa9\u7e23'), (11, '\u5609\u7fa9\u5e02'), (12, '\u53f0\u5357\u5e02'), (13, '\u9ad8\u96c4\u5e02'), (14, '\u5c4f\u6771\u7e23'), (15, '\u53f0\u6771\u7e23'), (16, '\u82b1\u84ee\u7e23'), (17, '\u5b9c\u862d\u7e23')])),
                ('breed', models.CharField(default=b'', max_length=20, verbose_name='\u54c1\u7a2e')),
                ('photo', models.ImageField(null=True, upload_to=b'pet')),
                ('pet_publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='pet',
            field=models.ForeignKey(to='pets_adopt.Pets'),
        ),
        migrations.AddField(
            model_name='adopt',
            name='adopt_pet',
            field=models.ForeignKey(to='pets_adopt.Pets'),
        ),
    ]
