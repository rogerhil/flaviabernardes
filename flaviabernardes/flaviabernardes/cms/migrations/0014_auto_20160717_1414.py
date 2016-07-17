# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20151121_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='background_cover',
            field=image_cropping.fields.ImageRatioField('background_cover_image', '1920x600', hide_image_field=False, adapt_rotation=False, size_warning=False, allow_fullsize=False, verbose_name='background cover', help_text=None, free_crop=False),
        ),
        migrations.AddField(
            model_name='page',
            name='background_cover_image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='page',
            name='show_footer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='page',
            name='show_header',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='background_cover',
            field=image_cropping.fields.ImageRatioField('background_cover_image', '1920x600', hide_image_field=False, adapt_rotation=False, size_warning=False, allow_fullsize=False, verbose_name='background cover', help_text=None, free_crop=False),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='background_cover_image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='show_footer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='show_header',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=128, editable=False, verbose_name='Slug', unique=True),
        ),
    ]
