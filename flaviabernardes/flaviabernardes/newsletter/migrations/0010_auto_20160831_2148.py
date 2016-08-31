# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_auto_20151119_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='sign_up_title',
            field=models.CharField(null=True, blank=True, max_length=255, default='Want an exclusive artwork wallpaper? Sign up below'),
            preserve_default=True,
        ),
    ]
