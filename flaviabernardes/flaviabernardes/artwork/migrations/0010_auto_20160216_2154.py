# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0009_auto_20160210_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagartwork',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='artwork',
            name='collector_contact',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='edition',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='exhibition',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='frame_cost',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='id_number',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='location',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='other_cost',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='sold',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='sold_by',
            field=models.CharField(max_length=128, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artwork',
            name='total_price',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='type',
            field=models.ForeignKey(verbose_name='Medium', to='artwork.ArtworkType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tagartwork',
            name='artwork',
            field=models.ForeignKey(to='artwork.Artwork', related_name='link_to_tag'),
            preserve_default=True,
        ),
    ]
