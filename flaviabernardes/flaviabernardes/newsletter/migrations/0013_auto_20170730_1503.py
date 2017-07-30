# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_auto_20170402_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(blank=True, verbose_name='Name', null=True, max_length=255),
        ),
    ]
