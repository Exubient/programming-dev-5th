# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_auto_20160722_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=8),
        ),
    ]
