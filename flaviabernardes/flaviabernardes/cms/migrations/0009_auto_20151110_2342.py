# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20151110_2339'),
        ('cms', '0008_auto_20151028_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='newsletter',
            field=models.ForeignKey(to='newsletter.List', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='newsletter',
            field=models.ForeignKey(to='newsletter.List', blank=True, null=True),
            preserve_default=True,
        ),
    ]
