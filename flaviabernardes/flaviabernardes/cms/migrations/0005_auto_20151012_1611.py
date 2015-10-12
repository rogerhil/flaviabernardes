# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20151012_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(max_length=255, help_text='Please consider filling this field to provide proper information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='description',
            field=models.CharField(max_length=255, help_text='Please consider filling this field to provide proper information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.'),
        ),
    ]
