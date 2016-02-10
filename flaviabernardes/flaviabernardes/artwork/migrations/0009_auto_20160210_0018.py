# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0008_auto_20151028_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagArtwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.IntegerField(default=0, editable=False)),
                ('artwork', models.ForeignKey(to='artwork.Artwork')),
                ('tag', models.ForeignKey(to='artwork.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artwork',
            name='tags',
            field=models.ManyToManyField(to='artwork.Tag', through='artwork.TagArtwork'),
            preserve_default=True,
        ),
    ]
