# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160831_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_top_banner',
            field=models.BooleanField(verbose_name='Show top banner', default=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='show_top_banner',
            field=models.BooleanField(verbose_name='Show top banner', default=True),
        ),
    ]
