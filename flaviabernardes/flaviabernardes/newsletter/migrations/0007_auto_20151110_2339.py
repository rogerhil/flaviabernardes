# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20151110_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='sign_up_title',
            field=models.CharField(max_length=255, default='Want an exclusive artwork wallpaper? Sign up below'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='list',
            name='confirmation_page',
            field=models.ForeignKey(null=True, to='cms.Page', related_name='confirmation_newsletter_lists', blank=True),
            preserve_default=True,
        ),
    ]
