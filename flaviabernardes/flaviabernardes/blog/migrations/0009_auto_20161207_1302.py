# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160717_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='newsletter_form_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='newsletter_form_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
