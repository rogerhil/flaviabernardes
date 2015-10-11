# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields
import flaviabernardes.cms.base


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageDraft',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image_banner1', models.ImageField(upload_to='uploads', blank=True)),
                ('image_banner2', models.ImageField(upload_to='uploads', blank=True)),
                ('image_social', models.ImageField(upload_to='uploads', blank=True)),
                ('banner1', image_cropping.fields.ImageRatioField('image_banner1', '1920x600', verbose_name='banner1', size_warning=False, free_crop=False, allow_fullsize=False, help_text=None, hide_image_field=False, adapt_rotation=False)),
                ('banner2', image_cropping.fields.ImageRatioField('image_banner2', '1920x600', verbose_name='banner2', size_warning=False, free_crop=False, allow_fullsize=False, help_text=None, hide_image_field=False, adapt_rotation=False)),
                ('social', image_cropping.fields.ImageRatioField('image_social', '1200x630', verbose_name='social', size_warning=False, free_crop=False, allow_fullsize=False, help_text=None, hide_image_field=False, adapt_rotation=False)),
                ('content1', models.TextField(null=True, blank=True)),
                ('content2', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=128, editable=False)),
                ('page', models.ForeignKey(null=True, blank=True, editable=False, to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, flaviabernardes.cms.base.CmsDraft),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=128, editable=False, unique=True),
            preserve_default=True,
        ),
    ]
