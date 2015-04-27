# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0003_artwork_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('artwork_related', models.ManyToManyField(to='artwork.Artwork')),
                ('related', models.ManyToManyField(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='uploads', blank=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('head_ratio', image_cropping.fields.ImageRatioField('image', '960x250', help_text=None, hide_image_field=False, free_crop=False, verbose_name='head ratio', size_warning=False, allow_fullsize=False, adapt_rotation=False)),
                ('half_ratio', image_cropping.fields.ImageRatioField('image', '470x250', help_text=None, hide_image_field=False, free_crop=False, verbose_name='half ratio', size_warning=False, allow_fullsize=False, adapt_rotation=False)),
                ('blog', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
            preserve_default=True,
        ),
    ]
