# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='name',
            field=models.CharField(default=b'\xe4\xbd\xa0\xe7\x9a\x84\xe5\xa4\xa7\xe5\x90\x8d', max_length=20, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='profile',
            field=models.TextField(verbose_name='\u500b\u4eba\u81ea\u8ff0'),
        ),
    ]
