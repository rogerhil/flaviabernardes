# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160717_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='banner_with_content',
            field=image_cropping.fields.ImageRatioField('image_banner_with_content', '1920x1200', verbose_name='banner with content', adapt_rotation=False, allow_fullsize=False, size_warning=False, free_crop=False, help_text=None, hide_image_field=False),
        ),
        migrations.AddField(
            model_name='draft',
            name='content_for_banner',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='draft',
            name='image_banner_with_content',
            field=models.ImageField(upload_to='uploads', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='banner_with_content',
            field=image_cropping.fields.ImageRatioField('image_banner_with_content', '1920x1200', verbose_name='banner with content', adapt_rotation=False, allow_fullsize=False, size_warning=False, free_crop=False, help_text=None, hide_image_field=False),
        ),
        migrations.AddField(
            model_name='post',
            name='content_for_banner',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_banner_with_content',
            field=models.ImageField(upload_to='uploads', blank=True),
        ),
    ]
