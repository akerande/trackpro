# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-05 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksheet', '0004_auto_20180405_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='correct_by',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='label_by',
        ),
        migrations.AddField(
            model_name='image',
            name='corrected_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='label_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
