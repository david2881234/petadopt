# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0017_auto_20151128_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='credit_bad',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='credit_good',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='credit_ok',
        ),
        migrations.AddField(
            model_name='comment',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='\u4fe1\u7528', choices=[(0, '\u512a\u826f'), (1, '\u666e\u901a'), (2, '\u4e0d\u826f')]),
        ),
    ]
