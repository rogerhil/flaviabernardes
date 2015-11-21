# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_auto_20151117_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='newsletter',
            field=models.ForeignKey(default=1, to='newsletter.List'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='newsletter',
            field=models.ForeignKey(default=1, to='newsletter.List'),
            preserve_default=True,
        ),
    ]
