# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 03:41
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='jjal',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=blog.models.random_name_upload_to),
        ),
    ]