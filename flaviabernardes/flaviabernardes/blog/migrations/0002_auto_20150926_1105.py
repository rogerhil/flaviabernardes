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
            name='banner',
            field=image_cropping.fields.ImageRatioField('image', '960x200', free_crop=False, help_text=None, hide_image_field=False, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='banner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='banner',
            field=image_cropping.fields.ImageRatioField('image', '960x200', free_crop=False, help_text=None, hide_image_field=False, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='banner'),
            preserve_default=True,
        ),
    ]
