# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20151121_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='newsletter',
            field=models.ForeignKey(to='newsletter.List', default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='newsletter',
            field=models.ForeignKey(to='newsletter.List', default=1),
            preserve_default=True,
        ),
    ]
