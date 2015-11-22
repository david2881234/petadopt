# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0012_auto_20151123_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='neuter',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u6709\u7d50\u7d2e', choices=[(True, '\u6709'), (False, '\u7121')]),
        ),
    ]
