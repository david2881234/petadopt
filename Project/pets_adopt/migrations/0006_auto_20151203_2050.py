# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pets_adopt', '0005_pets_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='pet_owner',
            field=models.ForeignKey(related_name='current_owner', default=b'', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_publisher',
            field=models.ForeignKey(related_name='previous_owner', default=b'', to=settings.AUTH_USER_MODEL),
        ),
    ]
