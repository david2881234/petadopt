# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0010_adopt'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='state',
        ),
        migrations.AddField(
            model_name='newuser',
            name='address',
            field=models.CharField(default=b'', max_length=50, verbose_name='\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='facebook',
            field=models.CharField(default=b'', max_length=20, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='home_tel',
            field=models.CharField(default=b'', max_length=11, verbose_name='\u5bb6\u96fb'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='id_card_num',
            field=models.CharField(default=b'', max_length=10, verbose_name='\u8eab\u4efd\u8b49\u5b57\u865f'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='line',
            field=models.CharField(default=b'', max_length=20, verbose_name='Line'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='mobile',
            field=models.CharField(default=b'', max_length=10, verbose_name='\u624b\u6a5f\u865f\u78bc'),
        ),
        migrations.AddField(
            model_name='pets',
            name='area',
            field=models.IntegerField(default=0, verbose_name='\u5bf5\u7269\u6240\u5728\u5730\u5340', choices=[(0, '\u53f0\u5317\u5e02'), (1, '\u65b0\u5317\u5e02'), (2, '\u6843\u5712\u5e02'), (3, '\u65b0\u7af9\u7e23'), (4, '\u65b0\u7af9\u5e02'), (5, '\u82d7\u6817\u7e23'), (6, '\u53f0\u4e2d\u5e02'), (7, '\u5f70\u5316\u7e23'), (8, '\u5357\u6295\u7e23'), (9, '\u96f2\u6797\u7e23'), (10, '\u5609\u7fa9\u7e23'), (11, '\u5609\u7fa9\u5e02'), (12, '\u53f0\u5357\u5e02'), (13, '\u9ad8\u96c4\u5e02'), (14, '\u5c4f\u6771\u7e23'), (15, '\u53f0\u6771\u7e23'), (16, '\u82b1\u84ee\u7e23'), (17, '\u5b9c\u862d\u7e23')]),
        ),
        migrations.AddField(
            model_name='pets',
            name='breed',
            field=models.CharField(default=b'', max_length=10, verbose_name='\u54c1\u7a2e'),
        ),
        migrations.AddField(
            model_name='pets',
            name='chip',
            field=models.BooleanField(default=False, verbose_name='\u6676\u7247\u6709\u7121', choices=[(True, '\u6709'), (False, '\u7121')]),
        ),
        migrations.AddField(
            model_name='pets',
            name='color',
            field=models.CharField(default=b'', max_length=5, verbose_name='\u6bdb\u8272'),
        ),
        migrations.AddField(
            model_name='pets',
            name='dog_or_cat',
            field=models.IntegerField(default=0, verbose_name='\u72d7\u6216\u8c93', choices=[(0, '\u72d7'), (1, '\u8c93')]),
        ),
        migrations.AddField(
            model_name='pets',
            name='image_file',
            field=models.FileField(null=True, upload_to=b'media/pet_image'),
        ),
        migrations.AddField(
            model_name='pets',
            name='neuter',
            field=models.BigIntegerField(default=False, verbose_name='\u662f\u5426\u6709\u7d50\u7d2e', choices=[(True, '\u6709'), (False, '\u7121')]),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='mode',
            field=models.IntegerField(default=0, verbose_name='\u5be9\u6838', choices=[(0, '\u5f85\u6279\u51c6'), (1, '\u901a\u904e'), (2, '\u62d2\u7d55'), (3, '\u5f85\u9818\u990a\u8005\u78ba\u8a8d'), (4, '\u5f85\u9001\u990a\u8005\u78ba\u8a8d')]),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='gender',
            field=models.CharField(default=b'm', max_length=1, verbose_name='\u6027\u5225', choices=[(b'm', '\u7537'), (b'f', '\u5973')]),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='name',
            field=models.CharField(default=b'', max_length=20, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='profile',
            field=models.TextField(default=b'', max_length=200, verbose_name='\u500b\u4eba\u81ea\u8ff0'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='content',
            field=models.TextField(max_length=300, verbose_name='\u5bf5\u7269\u7c21\u4ecb'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_name',
            field=models.CharField(default=b'', max_length=30, verbose_name='\u5bf5\u7269\u540d'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='pet',
            field=models.ForeignKey(to='pets_adopt.Pets'),
        ),
    ]
