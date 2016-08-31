# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20160717_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='box_background_color',
            field=colorfield.fields.ColorField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='box_opacity',
            field=models.FloatField(choices=[(0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)], blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='box_square',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='foreground_color',
            field=colorfield.fields.ColorField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='box_background_color',
            field=colorfield.fields.ColorField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='box_opacity',
            field=models.FloatField(choices=[(0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)], blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='box_square',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='foreground_color',
            field=colorfield.fields.ColorField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
    ]
