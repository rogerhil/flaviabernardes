# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150817_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='blog',
            field=models.ForeignKey(to='blog.Blog', null=True, blank=True),
        ),
    ]
