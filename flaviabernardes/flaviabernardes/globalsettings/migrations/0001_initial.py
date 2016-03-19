# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_auto_20151119_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('top_sign_up_title', models.CharField(max_length=255, default='Want an exclusive artwork wallpaper? Sign up below')),
                ('top_newsletter', models.ForeignKey(blank=True, to='newsletter.List', default=1, null=True, on_delete=models.SET(None))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
