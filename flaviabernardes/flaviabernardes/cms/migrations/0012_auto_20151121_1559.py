# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20151121_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagedraft',
            name='newsletter',
            field=models.ForeignKey(null=True, blank=True, to='newsletter.List', on_delete=models.SET(None), default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='page',
            field=models.ForeignKey(null=True, blank=True, to='cms.Page', editable=False, on_delete=models.SET(None)),
            preserve_default=True,
        ),
    ]
