# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-11 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0004_auto_20180523_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]