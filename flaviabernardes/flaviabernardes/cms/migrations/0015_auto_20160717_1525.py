# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160717_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content4',
            field=models.TextField(help_text='This content appears AFTER the NEWSLETTER form', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='content4',
            field=models.TextField(help_text='This content appears AFTER the NEWSLETTER form', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='background_cover',
            field=image_cropping.fields.ImageRatioField('background_cover_image', '1920x1200', hide_image_field=False, allow_fullsize=False, size_warning=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='background cover'),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer',
            field=models.BooleanField(default=False, verbose_name='Show this page link in footer'),
        ),
        migrations.AlterField(
            model_name='page',
            name='show_footer',
            field=models.BooleanField(default=True, verbose_name='Show site footer'),
        ),
        migrations.AlterField(
            model_name='page',
            name='show_header',
            field=models.BooleanField(default=True, verbose_name='Show site header'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='background_cover',
            field=image_cropping.fields.ImageRatioField('background_cover_image', '1920x1200', hide_image_field=False, allow_fullsize=False, size_warning=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='background cover'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='footer',
            field=models.BooleanField(default=False, verbose_name='Show this page link in footer'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='name',
            field=models.CharField(help_text="PLEASE PROVIDE A GOOD SLUG NAME FOR THIS PAGE IF YOU ARE CREATING A NEW ONE NOW, SO YOU WON'T NEED TO CHANGE IT ANYMORE IN THE FUTURE. THIS VALUE ALSO CORRESPONDS TO THE SLUG OF THE PAGE THAT WILL APPEAR IN THE URL (e.g.: /artworks/slug/) AND IT IS COMPLICATED TO CHANGE THIS VALUE AFTERWARDS. PLEASE AVOID CHANGING THIS VALUE BECAUSE IT CORRESPONDS TO THE SLUG OF THE SUB PAGE AND IT WILL AFFECT DISQUS COMMENTS REFERENCES AND GOOGLE INDEXING.", max_length=128, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='show_footer',
            field=models.BooleanField(default=True, verbose_name='Show site footer'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='show_header',
            field=models.BooleanField(default=True, verbose_name='Show site header'),
        ),
    ]
