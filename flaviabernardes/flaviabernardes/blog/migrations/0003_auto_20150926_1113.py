# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150926_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='listing_image',
            field=models.ImageField(upload_to='uploads', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='listing_image',
            field=models.ImageField(upload_to='uploads', blank=True),
            preserve_default=True,
        ),
    ]
