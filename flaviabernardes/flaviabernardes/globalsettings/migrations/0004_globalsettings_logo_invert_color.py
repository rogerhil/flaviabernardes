# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0003_auto_20170127_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='logo_invert_color',
            field=models.BooleanField(default=False),
        ),
    ]
