# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image_banner1', models.ImageField(blank=True, upload_to='uploads')),
                ('image_banner2', models.ImageField(blank=True, upload_to='uploads')),
                ('image_social', models.ImageField(blank=True, upload_to='uploads')),
                ('banner1', image_cropping.fields.ImageRatioField('image_banner1', '1920x600', size_warning=False, allow_fullsize=False, hide_image_field=False, help_text=None, adapt_rotation=False, free_crop=False, verbose_name='banner1')),
                ('banner2', image_cropping.fields.ImageRatioField('image_banner2', '1920x600', size_warning=False, allow_fullsize=False, hide_image_field=False, help_text=None, adapt_rotation=False, free_crop=False, verbose_name='banner2')),
                ('social', image_cropping.fields.ImageRatioField('image_social', '1200x630', size_warning=False, allow_fullsize=False, hide_image_field=False, help_text=None, adapt_rotation=False, free_crop=False, verbose_name='social')),
                ('content1', models.TextField(blank=True, null=True)),
                ('content2', models.TextField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
