# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0016_auto_20151128_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='\u8a55\u8a9e')),
                ('credit_good', models.IntegerField(default=0, verbose_name='\u512a\u826f\u4fe1\u7528')),
                ('credit_ok', models.IntegerField(default=0, verbose_name='\u666e\u901a\u4fe1\u7528')),
                ('credit_bad', models.IntegerField(default=0, verbose_name='\u4e0d\u826f\u4fe1\u7528')),
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='credit_good',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='credit_ok',
        ),
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
