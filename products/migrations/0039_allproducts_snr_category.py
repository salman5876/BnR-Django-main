# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20171213_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='SNR_Category',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
