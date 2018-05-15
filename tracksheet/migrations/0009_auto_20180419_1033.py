# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-19 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracksheet', '0008_auto_20180412_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracksheet.Folder'),
        ),
        migrations.AlterField(
            model_name='image',
            name='sequence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracksheet.Sequence'),
        ),
    ]
