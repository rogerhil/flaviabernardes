# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('list_id', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('uuid', models.CharField(unique=True, blank=True, default=uuid.uuid4, max_length=100)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('first_name', models.CharField(null=True, blank=True, max_length=255)),
                ('last_name', models.CharField(null=True, blank=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('list', models.ForeignKey(to='newsletter.List')),
                ('subscriber', models.ForeignKey(to='newsletter.Subscriber')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
