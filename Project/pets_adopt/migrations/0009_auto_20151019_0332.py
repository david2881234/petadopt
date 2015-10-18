# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0008_auto_20151019_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='state',
            field=models.IntegerField(default=0, verbose_name='\u9818\u990a\u72c0\u614b', choices=[(0, '\u5f85\u8a8d\u990a'), (1, '\u5df2\u9818\u990a')]),
        ),
    ]
