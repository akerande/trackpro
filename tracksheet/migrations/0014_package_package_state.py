# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-05 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksheet', '0013_auto_20180504_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_state',
            field=models.CharField(blank=True, choices=[('rework', 'rework'), ('practice', 'practice')], max_length=15, null=True),
        ),
    ]
