# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150817_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image', '300x300', free_crop=False, allow_fullsize=False, help_text=None, verbose_name='listing', size_warning=False, adapt_rotation=False, hide_image_field=False),
        ),
        migrations.AddField(
            model_name='draft',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image', '300x300', free_crop=False, allow_fullsize=False, help_text=None, verbose_name='listing', size_warning=False, adapt_rotation=False, hide_image_field=False),
        ),
    ]
