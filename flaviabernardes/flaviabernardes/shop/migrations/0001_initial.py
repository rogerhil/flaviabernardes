# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0011_auto_20160217_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Original',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('link', models.URLField()),
                ('order', models.IntegerField(default=0, editable=False)),
                ('artwork', models.ForeignKey(to='artwork.Artwork')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)),
                ('price_from', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)),
                ('price_to', models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)),
                ('sizes', models.TextField()),
                ('link', models.URLField()),
                ('order', models.IntegerField(default=0, editable=False)),
                ('artwork', models.ForeignKey(to='artwork.Artwork')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
