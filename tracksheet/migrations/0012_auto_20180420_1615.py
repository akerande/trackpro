# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-20 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksheet', '0011_auto_20180420_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='approved_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='corrected_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_by',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='label_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_by',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]