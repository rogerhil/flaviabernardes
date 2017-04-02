# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalsettings', '0006_globalsettings_javascript_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='javascript_codes_ignore_landing_pages',
            field=models.TextField(null=True, help_text="Same as above, except that the codes won't be put on landing pages (without HEADER and FOOTER)", blank=True),
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='javascript_codes',
            field=models.TextField(null=True, help_text='Embed JavaScript codes (privy, smartlook, etc) that will be available in EVERY page.', blank=True),
        ),
    ]
