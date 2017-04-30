# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0007_auto_20170402_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='global_keywords',
            field=models.TextField(null=True, help_text='Keywords separated by comma, e.g: fine arts, oil pastel, watercolour', blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_description',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='main_title',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
    ]
