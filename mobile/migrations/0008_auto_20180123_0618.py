# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0007_auto_20170911_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_db',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mobile_db',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='mobile_db',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
    ]
