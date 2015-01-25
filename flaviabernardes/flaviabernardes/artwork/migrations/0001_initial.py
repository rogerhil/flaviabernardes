# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to='uploads', blank=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('year', models.IntegerField()),
                ('listing', models.BooleanField(default=True)),
                ('home', models.BooleanField(default=False)),
                ('mini_thumbnail', image_cropping.fields.ImageRatioField('image', '50x50', verbose_name='mini thumbnail', free_crop=False, adapt_rotation=False, hide_image_field=False, help_text=None, allow_fullsize=False, size_warning=False)),
                ('thumbnail', image_cropping.fields.ImageRatioField('image', '125x125', verbose_name='thumbnail', free_crop=False, adapt_rotation=False, hide_image_field=False, help_text=None, allow_fullsize=False, size_warning=True)),
                ('listing_preview', image_cropping.fields.ImageRatioField('image', '525x580', verbose_name='listing preview', free_crop=False, adapt_rotation=False, hide_image_field=False, help_text=None, allow_fullsize=False, size_warning=True)),
                ('home_preview', image_cropping.fields.ImageRatioField('image', '960x580', verbose_name='home preview', free_crop=False, adapt_rotation=False, hide_image_field=False, help_text=None, allow_fullsize=False, size_warning=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArtworkType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artwork',
            name='type',
            field=models.ForeignKey(to='artwork.ArtworkType'),
            preserve_default=True,
        ),
    ]
