# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160831_2219'),
        ('globalsettings', '0004_globalsettings_logo_invert_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='menu_1',
            field=models.ForeignKey(to='cms.Page', null=True, blank=True, related_name='menu_1_global_setting'),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_2',
            field=models.ForeignKey(to='cms.Page', null=True, blank=True, related_name='menu_2_global_setting'),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_3',
            field=models.ForeignKey(to='cms.Page', null=True, blank=True, related_name='menu_3_global_setting'),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_4',
            field=models.ForeignKey(to='cms.Page', null=True, blank=True, related_name='menu_4_global_setting'),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='menu_5',
            field=models.ForeignKey(to='cms.Page', null=True, blank=True, related_name='menu_5_global_setting'),
        ),
    ]
