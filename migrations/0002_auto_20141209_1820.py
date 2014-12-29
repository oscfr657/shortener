# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.URLField(max_length=256, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='word',
            field=models.CharField(unique=True, max_length=64),
            preserve_default=True,
        ),
    ]
