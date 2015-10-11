# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20151011_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 11, 18, 45, 42, 152605)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 11, 18, 45, 42, 152636)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 11, 18, 45, 42, 152605)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 11, 18, 45, 42, 152636)),
            preserve_default=True,
        ),
    ]
