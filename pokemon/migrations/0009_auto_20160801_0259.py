# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import pokemon.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_auto_20160801_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='post_number',
            field=models.IntegerField(validators=[pokemon.validators.post()]),
        ),
    ]
