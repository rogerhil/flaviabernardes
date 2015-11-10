# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20151028_1931'),
        ('newsletter', '0005_auto_20150927_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='confirmation_page',
            field=models.ForeignKey(null=True, blank=True, to='cms.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='email_message',
            field=models.TextField(default="<p>Hello %(name)s,</p>\n<p>Please follow the link below.</p>\n<p>If you can't click it, please copy the entire link and paste it into your\nbrowser.</p>\n<p>%(link)s</p>\n<p>Thank you,</p>\n<p>Flavia Bernardes</p>\n"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='email_subject',
            field=models.CharField(max_length=255, default='Confirm your subscription'),
            preserve_default=True,
        ),
    ]
