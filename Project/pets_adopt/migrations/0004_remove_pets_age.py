# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0003_auto_20151203_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='age',
        ),
    ]
