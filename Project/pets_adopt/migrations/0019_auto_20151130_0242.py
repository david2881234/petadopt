# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0018_auto_20151128_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='image_file',
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'article'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='photo',
            field=models.ImageField(upload_to=b'person', null=True, verbose_name='\u7167\u7247'),
        ),
        migrations.AddField(
            model_name='pets',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'pet'),
        ),
    ]
