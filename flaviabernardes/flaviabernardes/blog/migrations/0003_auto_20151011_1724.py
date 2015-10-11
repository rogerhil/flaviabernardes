# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151010_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x600', help_text=None, hide_image_field=False, size_warning=False, adapt_rotation=False, free_crop=False, verbose_name='banner2', allow_fullsize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='banner2',
            field=image_cropping.fields.ImageRatioField('image_banner2', '1920x600', help_text=None, hide_image_field=False, size_warning=False, adapt_rotation=False, free_crop=False, verbose_name='banner2', allow_fullsize=False),
            preserve_default=True,
        ),
    ]
