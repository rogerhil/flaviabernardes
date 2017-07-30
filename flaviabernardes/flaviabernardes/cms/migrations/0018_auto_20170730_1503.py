# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20170423_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='newsletter_submit_button_color',
            field=colorfield.fields.ColorField(blank=True, verbose_name='Newsletter submit button color', null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='page',
            name='newsletter_submit_button_opacity',
            field=models.FloatField(blank=True, null=True, choices=[(0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)]),
        ),
        migrations.AddField(
            model_name='page',
            name='show_newsletter_name_field',
            field=models.BooleanField(verbose_name='Show newsletter name field', default=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='newsletter_submit_button_color',
            field=colorfield.fields.ColorField(blank=True, verbose_name='Newsletter submit button color', null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='newsletter_submit_button_opacity',
            field=models.FloatField(blank=True, null=True, choices=[(0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)]),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='show_newsletter_name_field',
            field=models.BooleanField(verbose_name='Show newsletter name field', default=True),
        ),
    ]
