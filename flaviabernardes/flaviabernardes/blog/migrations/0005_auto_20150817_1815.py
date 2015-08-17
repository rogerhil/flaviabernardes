# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150817_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='uploads', blank=True),
        ),
        migrations.AddField(
            model_name='draft',
            name='image',
            field=models.ImageField(upload_to='uploads', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='blog',
            field=models.ForeignKey(to='blog.Blog', related_name='images'),
        ),
    ]
