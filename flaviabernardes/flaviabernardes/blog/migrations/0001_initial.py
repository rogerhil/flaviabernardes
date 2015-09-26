# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('listing', image_cropping.fields.ImageRatioField('image', '300x300', hide_image_field=False, help_text=None, free_crop=False, verbose_name='listing', size_warning=False, adapt_rotation=False, allow_fullsize=False)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DraftImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('ratio', image_cropping.fields.ImageRatioField('image', '50x50', hide_image_field=False, help_text=None, free_crop=False, verbose_name='ratio', size_warning=False, adapt_rotation=False, allow_fullsize=False)),
                ('draft', models.ForeignKey(to='blog.Draft')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('ratio', image_cropping.fields.ImageRatioField('image', '50x50', hide_image_field=False, help_text=None, free_crop=False, verbose_name='ratio', size_warning=False, adapt_rotation=False, allow_fullsize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('listing', image_cropping.fields.ImageRatioField('image', '300x300', hide_image_field=False, help_text=None, free_crop=False, verbose_name='listing', size_warning=False, adapt_rotation=False, allow_fullsize=False)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='images'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='draft',
            name='post',
            field=models.ForeignKey(to='blog.Post', blank=True, editable=False, null=True),
            preserve_default=True,
        ),
    ]
