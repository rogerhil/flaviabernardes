# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='original',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='original',
            name='thumbnail',
            field=image_cropping.fields.ImageRatioField('image', '640x400', help_text=None, hide_image_field=False, free_crop=False, size_warning=True, adapt_rotation=False, verbose_name='thumbnail', allow_fullsize=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='print',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='print',
            name='thumbnail',
            field=image_cropping.fields.ImageRatioField('image', '640x400', help_text=None, hide_image_field=False, free_crop=False, size_warning=True, adapt_rotation=False, verbose_name='thumbnail', allow_fullsize=False),
            preserve_default=True,
        ),
    ]
