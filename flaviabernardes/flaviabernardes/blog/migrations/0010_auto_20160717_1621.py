# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160717_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='text4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text4',
            field=models.TextField(blank=True, null=True),
        ),
    ]
