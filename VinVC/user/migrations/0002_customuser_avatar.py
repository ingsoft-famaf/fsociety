# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=user.models.avatar_directory_path),
        ),
    ]