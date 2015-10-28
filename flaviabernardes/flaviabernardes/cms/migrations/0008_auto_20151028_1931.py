# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20151027_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagedraft',
            name='name',
            field=models.CharField(max_length=128, help_text="PLEASE PROVIDE A GOOD NAME FOR THIS PAGE IF YOU ARE CREATING A NEW ONE NOW, SO YOU WON'T NEED TO CHANGE IT ANYMORE IN THE FUTURE. THIS VALUE ALSO CORRESPONDS TO THE SLUG OF THE PAGE THAT WILL APPEAR IN THE URL (e.g.: /artworks/slug/) AND IT IS COMPLICATED TO CHANGE THIS VALUE AFTERWARDS. PLEASE AVOID CHANGING THIS VALUE BECAUSE IT CORRESPONDS TO THE SLUG OF THE SUB PAGE AND IT WILL AFFECT DISQUS COMMENTS REFERENCES AND GOOGLE INDEXING."),
            preserve_default=True,
        ),
    ]
