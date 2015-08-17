# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150315_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DraftImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('ratio', image_cropping.fields.ImageRatioField('image', '50x50', adapt_rotation=False, size_warning=False, allow_fullsize=False, hide_image_field=False, verbose_name='ratio', free_crop=False, help_text=None)),
                ('draft', models.ForeignKey(to='blog.Draft')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='artwork_related',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='related',
        ),
        migrations.RemoveField(
            model_name='image',
            name='half_ratio',
        ),
        migrations.RemoveField(
            model_name='image',
            name='head_ratio',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='ratio',
            field=image_cropping.fields.ImageRatioField('image', '50x50', adapt_rotation=False, size_warning=False, allow_fullsize=False, hide_image_field=False, verbose_name='ratio', free_crop=False, help_text=None),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='draft',
            name='blog',
            field=models.ForeignKey(to='blog.Blog'),
        ),
    ]
