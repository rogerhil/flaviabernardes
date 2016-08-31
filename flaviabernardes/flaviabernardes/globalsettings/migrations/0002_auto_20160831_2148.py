# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='top_newsletter',
            field=models.ForeignKey(to='newsletter.List', on_delete=models.SET(None), default=1, null=True, blank=True, help_text='Choose the Newsletter list to be used at the Top Bar form.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='top_sign_up_title',
            field=models.CharField(help_text='A short description to appear to the left side of thenewsletter form at the Top Bar.', max_length=255, default='Want an exclusive artwork wallpaper? Sign up below'),
            preserve_default=True,
        ),
    ]
