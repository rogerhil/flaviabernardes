# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160314_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='original',
            name='disable',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='print',
            name='disable',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
