# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_auto_20141209_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shorturl',
            options={'ordering': ['-word']},
        ),
        migrations.AddField(
            model_name='shorturl',
            name='changed_at_date_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 22, 56, 23, 494187), auto_now=True),
            preserve_default=True,
        ),
    ]
