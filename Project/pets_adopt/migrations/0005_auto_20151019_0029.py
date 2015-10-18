# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0004_newuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u59d3\u540d'),
        ),
    ]
