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
            model_name='image',
            name='listing',
            field=image_cropping.fields.ImageRatioField('image', '305x305', help_text=None, free_crop=False, hide_image_field=False, verbose_name='listing', size_warning=False, allow_fullsize=False, adapt_rotation=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='artwork_related',
            field=models.ManyToManyField(to='artwork.Artwork', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='related',
            field=models.ManyToManyField(to='blog.Blog', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='half_ratio',
            field=image_cropping.fields.ImageRatioField('image', '460x250', help_text=None, free_crop=False, hide_image_field=False, verbose_name='half ratio', size_warning=False, allow_fullsize=False, adapt_rotation=False),
            preserve_default=True,
        ),
    ]
