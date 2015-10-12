# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151011_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='description',
            field=models.CharField(blank=True, help_text='Please consider filling this field to provide information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='Please consider filling this field to provide information to social media, e.g.: Facebook share. This description will included as a <meta> tag in the html to be parsed when the url is shared through a social website.', max_length=255, null=True),
        ),
    ]
