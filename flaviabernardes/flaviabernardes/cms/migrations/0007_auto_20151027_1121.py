# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20151014_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sub_page_of',
            field=models.ForeignKey(null=True, blank=True, to='cms.Page'),
        ),
        migrations.AddField(
            model_name='pagedraft',
            name='sub_page_of',
            field=models.ForeignKey(null=True, blank=True, to='cms.Page', related_name='pages_sub'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content2',
            field=models.TextField(null=True, blank=True, help_text='This content appears BEFORE the SECOND banner'),
        ),
        migrations.AlterField(
            model_name='pagedraft',
            name='content2',
            field=models.TextField(null=True, blank=True, help_text='This content appears BEFORE the SECOND banner'),
        ),
    ]
