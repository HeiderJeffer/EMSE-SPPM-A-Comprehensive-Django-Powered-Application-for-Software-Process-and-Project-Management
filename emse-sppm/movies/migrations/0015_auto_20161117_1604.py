# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20161117_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default='0'),
        ),
    ]
