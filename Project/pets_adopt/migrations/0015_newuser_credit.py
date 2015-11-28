# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0014_auto_20151123_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='\u4fe1\u7528'),
        ),
    ]
