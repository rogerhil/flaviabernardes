# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20151110_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='provider',
            field=models.CharField(default='madmimi', editable=False, max_length=32),
            preserve_default=True,
        ),
    ]
