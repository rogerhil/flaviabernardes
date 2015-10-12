# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0006_auto_20151010_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='thumbnail',
            field=image_cropping.fields.ImageRatioField('image', '640x400', hide_image_field=False, adapt_rotation=False, size_warning=True, verbose_name='thumbnail', help_text=None, allow_fullsize=False, free_crop=False),
        ),
    ]
