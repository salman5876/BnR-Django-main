# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-06 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wearables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wearable_db',
            name='SNR_Price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=50),
        ),
    ]
