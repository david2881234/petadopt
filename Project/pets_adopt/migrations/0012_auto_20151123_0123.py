# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0011_auto_20151119_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='breed',
            field=models.CharField(default=b'', max_length=20, verbose_name='\u54c1\u7a2e'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='content',
            field=models.TextField(verbose_name='\u5bf5\u7269\u7c21\u4ecb'),
        ),
    ]
