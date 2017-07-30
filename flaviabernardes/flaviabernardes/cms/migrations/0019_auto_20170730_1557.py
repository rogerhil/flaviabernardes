# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_auto_20170730_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_newsletter_form_inline',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='show_newsletter_form_inline',
            field=models.BooleanField(default=True),
        ),
    ]
