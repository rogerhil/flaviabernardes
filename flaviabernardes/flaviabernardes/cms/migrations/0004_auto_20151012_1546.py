# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20151011_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(help_text='Please consider filling this field to provide information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='description',
            field=models.CharField(help_text='Please consider filling this field to provide information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.', max_length=255),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
