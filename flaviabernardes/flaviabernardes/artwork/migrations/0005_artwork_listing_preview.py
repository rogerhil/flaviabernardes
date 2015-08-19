# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0004_auto_20150817_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='listing_preview',
            field=image_cropping.fields.ImageRatioField('image', '510x580', adapt_rotation=False, allow_fullsize=False, size_warning=True, verbose_name='listing preview', hide_image_field=False, free_crop=False, help_text=None),
            preserve_default=True,
        ),
    ]
