# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='full_preview',
            field=image_cropping.fields.ImageRatioField('image', '960x580', help_text=None, free_crop=True, verbose_name='full preview', size_warning=False, hide_image_field=False, allow_fullsize=False, adapt_rotation=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='listing_preview',
            field=image_cropping.fields.ImageRatioField('image', '510x580', help_text=None, free_crop=False, verbose_name='listing preview', size_warning=True, hide_image_field=False, allow_fullsize=False, adapt_rotation=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='thumbnail',
            field=image_cropping.fields.ImageRatioField('image', '130x130', help_text=None, free_crop=False, verbose_name='thumbnail', size_warning=True, hide_image_field=False, allow_fullsize=False, adapt_rotation=False),
            preserve_default=True,
        ),
    ]
