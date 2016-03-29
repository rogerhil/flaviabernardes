# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160322_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='original',
            name='description',
            field=models.CharField(max_length=64, help_text="If there's no artwork associated with this shop item, this field must be filled with the following information: 'media type' and the 'size'.", blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='original',
            name='name',
            field=models.CharField(max_length=64, help_text="Please fill this field in case there's no artwork associated with this shop item.", blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='print',
            name='name',
            field=models.CharField(max_length=64, help_text="Please fill this field in case there's no artwork associated with this shop item.", blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='original',
            name='artwork',
            field=models.ForeignKey(null=True, blank=True, to='artwork.Artwork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='original',
            name='price',
            field=models.DecimalField(help_text='Price in euros', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='print',
            name='artwork',
            field=models.ForeignKey(null=True, blank=True, to='artwork.Artwork'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='print',
            name='price',
            field=models.DecimalField(max_digits=10, null=True, help_text='Price in euros', blank=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='print',
            name='price_from',
            field=models.DecimalField(max_digits=10, null=True, help_text='Price in euros', blank=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='print',
            name='price_to',
            field=models.DecimalField(max_digits=10, null=True, help_text='Price in euros', blank=True, decimal_places=2),
            preserve_default=True,
        ),
    ]
