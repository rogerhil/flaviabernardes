# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151121_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
