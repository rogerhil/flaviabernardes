# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20151117_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='confirmation_page',
            field=models.ForeignKey(related_name='confirmation_newsletter_lists', default=1, to='cms.Page'),
            preserve_default=False,
        ),
    ]
