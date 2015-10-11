# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_artwork_listing_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='listing_preview',
        ),
        migrations.AlterField(
            model_name='artwork',
            name='thumbnail',
            field=image_cropping.fields.ImageRatioField('image', '360x310', size_warning=True, verbose_name='thumbnail', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False),
            preserve_default=True,
        ),
    ]
