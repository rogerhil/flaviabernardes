# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20170127_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='provider',
            field=models.CharField(max_length=32, default='mailerlite', editable=False),
        ),
    ]
