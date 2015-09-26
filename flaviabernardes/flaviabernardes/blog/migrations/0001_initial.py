# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_banner', models.ImageField(upload_to='uploads', blank=True)),
                ('image_listing', models.ImageField(upload_to='uploads', blank=True)),
                ('listing', image_cropping.fields.ImageRatioField('listing_image', '305x305', hide_image_field=False, free_crop=False, help_text=None, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='listing')),
                ('banner', image_cropping.fields.ImageRatioField('image', '960x200', hide_image_field=False, free_crop=False, help_text=None, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='banner')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_banner', models.ImageField(upload_to='uploads', blank=True)),
                ('image_listing', models.ImageField(upload_to='uploads', blank=True)),
                ('listing', image_cropping.fields.ImageRatioField('listing_image', '305x305', hide_image_field=False, free_crop=False, help_text=None, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='listing')),
                ('banner', image_cropping.fields.ImageRatioField('image', '960x200', hide_image_field=False, free_crop=False, help_text=None, adapt_rotation=False, allow_fullsize=False, size_warning=False, verbose_name='banner')),
                ('title', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('tags', models.ManyToManyField(to='blog.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='draft',
            name='post',
            field=models.ForeignKey(null=True, to='blog.Post', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='draft',
            name='tags',
            field=models.ManyToManyField(to='blog.Category'),
            preserve_default=True,
        ),
    ]
