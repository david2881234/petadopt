# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0006_auto_20151203_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='size',
            field=models.IntegerField(default=0, verbose_name='\u9ad4\u578b', choices=[(0, '\u5c0f\u578b'), (1, '\u4e2d\u578b'), (2, '\u5927\u578b')]),
        ),
    ]
