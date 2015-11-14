# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20151028_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='footer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='footer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
