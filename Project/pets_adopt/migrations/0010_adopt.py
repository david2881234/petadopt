# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0009_auto_20151019_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.IntegerField(default=0, verbose_name='\u5be9\u6838', choices=[(0, '\u5f85\u6279\u51c6'), (1, '\u901a\u904e'), (2, '\u62d2\u7d55')])),
                ('content', models.TextField(verbose_name='\u8a8d\u990a\u7406\u7531')),
                ('adopt_person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('adopt_pet', models.ForeignKey(to='pets_adopt.Pets')),
            ],
        ),
    ]
