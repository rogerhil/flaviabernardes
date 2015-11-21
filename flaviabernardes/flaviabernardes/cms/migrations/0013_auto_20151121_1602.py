# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20151121_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='newsletter',
            field=models.ForeignKey(null=True, blank=True, on_delete=models.SET(None), default=1, to='newsletter.List'),
            preserve_default=True,
        ),
    ]
