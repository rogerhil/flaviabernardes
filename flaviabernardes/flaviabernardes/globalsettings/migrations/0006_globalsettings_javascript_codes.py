# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0005_auto_20170212_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='javascript_codes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
