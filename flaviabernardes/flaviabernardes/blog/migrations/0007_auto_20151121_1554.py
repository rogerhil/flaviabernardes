# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151027_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='post',
            field=models.ForeignKey(on_delete=models.SET(None), to='blog.Post', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
