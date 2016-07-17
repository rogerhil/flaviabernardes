# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20160717_1658'),
        ('blog', '0010_auto_20160717_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='draft',
            name='banner_newsletter',
            field=models.ForeignKey(null=True, blank=True, to='newsletter.List', on_delete=models.SET(None), default=1),
        ),
        migrations.AlterField(
            model_name='draft',
            name='text',
            field=models.TextField(help_text='Content after the FIRST banner'),
        ),
        migrations.AlterField(
            model_name='draft',
            name='text2',
            field=models.TextField(null=True, help_text='Content after the BANNER WITH CONTENT **IF THERE IS ONE**', blank=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='text3',
            field=models.TextField(null=True, help_text='Content after the SECOND banner', blank=True),
        ),
        migrations.AlterField(
            model_name='draft',
            name='text4',
            field=models.TextField(null=True, help_text='Content after the GREY newsletter near the footer', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Content after the FIRST banner'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text2',
            field=models.TextField(null=True, help_text='Content after the BANNER WITH CONTENT **IF THERE IS ONE**', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text3',
            field=models.TextField(null=True, help_text='Content after the SECOND banner', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text4',
            field=models.TextField(null=True, help_text='Content after the GREY newsletter near the footer', blank=True),
        ),
    ]
