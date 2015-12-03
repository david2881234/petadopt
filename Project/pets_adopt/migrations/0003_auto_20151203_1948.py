# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0002_auto_20151203_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='sex',
            field=models.BooleanField(default=True, verbose_name='\u5bf5\u7269\u6027\u5225', choices=[(True, '\u7537\u751f'), (False, '\u5973\u751f')]),
        ),
    ]
