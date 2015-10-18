# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0005_auto_20151019_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_name', models.CharField(max_length=30, verbose_name='\u5bf5\u7269\u540d')),
                ('state', models.CharField(default=b'0', max_length=1, verbose_name='\u9818\u990a\u72c0\u614b', choices=[(0, '\u5f85\u8a8d\u990a'), (1, '\u5df2\u9818\u990a')])),
                ('content', models.TextField(verbose_name='\u5bf5\u7269\u7c21\u4ecb')),
                ('pet_publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
