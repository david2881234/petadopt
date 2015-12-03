# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='age',
            field=models.IntegerField(default=0, verbose_name='\u5e74\u7d00', choices=[(0, '\u5e7c\u5e74'), (1, '\u6210\u5e74')]),
        ),
        migrations.AddField(
            model_name='pets',
            name='sex',
            field=models.BigIntegerField(default=True, verbose_name='\u5bf5\u7269\u6027\u5225', choices=[(True, '\u7537\u751f'), (False, '\u5973\u751f')]),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='mode',
            field=models.IntegerField(default=0, verbose_name='\u5be9\u6838\u72c0\u614b', choices=[(0, '\u5f85\u6279\u51c6'), (1, '\u901a\u904e'), (2, '\u62d2\u7d55'), (3, '\u5f85\u9818\u990a\u8005\u78ba\u8a8d'), (4, '\u5f85\u9001\u990a\u8005\u78ba\u8a8d')]),
        ),
        migrations.AlterField(
            model_name='pets',
            name='color',
            field=models.IntegerField(default=0, verbose_name='\u6bdb\u8272', choices=[(0, '\u767d\u8272'), (1, '\u9ed1\u8272'), (2, '\u68d5\u8272'), (3, '\u9ec3\u8272'), (4, '\u82b1\u8272'), (5, '\u864e\u73ed'), (6, '\u5176\u4ed6')]),
        ),
    ]
