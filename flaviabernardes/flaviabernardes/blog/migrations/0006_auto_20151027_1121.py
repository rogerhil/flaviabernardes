# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151012_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x1200', help_text=None, adapt_rotation=False, hide_image_field=False, allow_fullsize=False, free_crop=False, verbose_name='banner2', size_warning=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x1200', help_text=None, adapt_rotation=False, hide_image_field=False, allow_fullsize=False, free_crop=False, verbose_name='banner2', size_warning=False),
        ),
    ]
