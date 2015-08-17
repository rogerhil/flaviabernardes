# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_artwork_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='home_preview',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='listing_preview',
        ),
    ]
