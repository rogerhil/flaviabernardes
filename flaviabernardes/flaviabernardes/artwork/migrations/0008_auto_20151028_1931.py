# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0007_auto_20151012_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='home',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='order',
            field=models.IntegerField(editable=False, default=0),
            preserve_default=True,
        ),
    ]
