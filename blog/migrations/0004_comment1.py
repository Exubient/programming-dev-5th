# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_title2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
    ]