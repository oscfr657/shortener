# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=256, null=True, blank=True)),
            ],
            options={
                'ordering': ['word'],
            },
            bases=(models.Model,),
        ),
    ]
