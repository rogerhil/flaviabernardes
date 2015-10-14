# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20151012_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content3',
            field=models.TextField(blank=True, help_text='This content appears AFTER the SECOND banner', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='content3',
            field=models.TextField(blank=True, help_text='This content appears AFTER the SECOND banner', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x1200', allow_fullsize=False, adapt_rotation=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='banner2', free_crop=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content1',
            field=models.TextField(blank=True, help_text='This content appears AFTER the FIRST banner', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content2',
            field=models.TextField(blank=True, help_text='This content appears BEFORE the FIRST banner', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x1200', allow_fullsize=False, adapt_rotation=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='banner2', free_crop=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='content1',
            field=models.TextField(blank=True, help_text='This content appears AFTER the FIRST banner', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='content2',
            field=models.TextField(blank=True, help_text='This content appears BEFORE the FIRST banner', null=True),
            preserve_default=True,
        ),
    ]
