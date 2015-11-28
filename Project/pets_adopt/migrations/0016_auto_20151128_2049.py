# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0015_newuser_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='credit',
        ),
        migrations.AddField(
            model_name='newuser',
            name='credit_good',
            field=models.IntegerField(default=0, verbose_name='\u512a\u826f\u4fe1\u7528'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='credit_ok',
            field=models.IntegerField(default=0, verbose_name='\u666e\u901a\u4fe1\u7528'),
        ),
    ]
