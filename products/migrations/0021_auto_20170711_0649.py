# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-11 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20170706_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogames',
            name='SNR_Price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=50, null=True),
        ),
    ]
