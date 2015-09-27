# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20150820_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='provider',
            field=models.CharField(max_length=32, default='madmimi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='registered',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscription',
            name='joined',
            field=models.DateTimeField(null=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('list', 'subscriber')]),
        ),
    ]
