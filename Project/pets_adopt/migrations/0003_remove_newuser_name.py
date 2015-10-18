# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0002_auto_20151018_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='name',
        ),
    ]
