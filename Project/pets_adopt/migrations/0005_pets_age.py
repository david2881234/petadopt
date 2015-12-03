# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0004_remove_pets_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='age',
            field=models.IntegerField(default=0, verbose_name='\u5e74\u7d00', choices=[(0, '\u5e7c\u5e74'), (1, '\u6210\u5e74')]),
        ),
    ]
