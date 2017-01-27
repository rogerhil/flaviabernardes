# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0002_auto_20160831_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='foreground_color',
            field=colorfield.fields.ColorField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_1',
            field=image_cropping.fields.ImageRatioField('main_page_bg_image_1', '1920x1200', allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, verbose_name='main page bg 1', size_warning=False, adapt_rotation=False),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_2',
            field=image_cropping.fields.ImageRatioField('main_page_bg_image_2', '1920x1200', allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, verbose_name='main page bg 2', size_warning=False, adapt_rotation=False),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_3',
            field=image_cropping.fields.ImageRatioField('main_page_bg_image_3', '1920x1200', allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, verbose_name='main page bg 3', size_warning=False, adapt_rotation=False),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_4',
            field=image_cropping.fields.ImageRatioField('main_page_bg_image_4', '1920x1200', allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, verbose_name='main page bg 4', size_warning=False, adapt_rotation=False),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_5',
            field=image_cropping.fields.ImageRatioField('main_page_bg_image_5', '1920x1200', allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, verbose_name='main page bg 5', size_warning=False, adapt_rotation=False),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_image_1',
            field=models.ImageField(upload_to='uploads/main_page/', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_image_2',
            field=models.ImageField(upload_to='uploads/main_page/', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_image_3',
            field=models.ImageField(upload_to='uploads/main_page/', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_image_4',
            field=models.ImageField(upload_to='uploads/main_page/', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_page_bg_image_5',
            field=models.ImageField(upload_to='uploads/main_page/', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_bar_background_color',
            field=colorfield.fields.ColorField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_bar_opacity',
            field=models.FloatField(null=True, blank=True, choices=[(0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)]),
        ),
    ]
