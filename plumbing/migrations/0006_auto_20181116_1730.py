# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-16 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plumbing', '0005_auto_20181022_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='plumbing',
            name='priority',
            field=models.CharField(choices=[('EMERGENCY', 'EMERGENCY'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='EMERGENCY', max_length=30),
        ),
        migrations.AlterField(
            model_name='plumbing',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'IN_PROGRESS'), ('QUEUE', 'QUEUE'), ('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED')], default='QUEUE', max_length=30),
        ),
    ]