# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner', '1920x600', size_warning=False, verbose_name='banner2', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='draft',
            name='image_banner2',
            field=models.ImageField(blank=True, upload_to='uploads'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='draft',
            name='listing_half',
            field=image_cropping.fields.ImageRatioField('image_listing', '960x600', size_warning=False, verbose_name='listing half', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner', '1920x600', size_warning=False, verbose_name='banner2', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='image_banner2',
            field=models.ImageField(blank=True, upload_to='uploads'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='listing_half',
            field=image_cropping.fields.ImageRatioField('image_listing', '960x600', size_warning=False, verbose_name='listing half', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='draft',
            name='banner',
            field=image_cropping.fields.ImageRatioField('image_banner', '1920x600', size_warning=False, verbose_name='banner', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='draft',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image_listing', '1920x600', size_warning=False, verbose_name='listing', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=image_cropping.fields.ImageRatioField('image_banner', '1920x600', size_warning=False, verbose_name='banner', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image_listing', '1920x600', size_warning=False, verbose_name='listing', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
    ]
