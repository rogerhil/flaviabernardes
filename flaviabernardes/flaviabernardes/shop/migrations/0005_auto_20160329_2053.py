# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160329_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='original',
            name='sold_out',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='print',
            name='sold_out',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
