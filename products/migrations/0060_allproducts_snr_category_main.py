# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0059_auto_20181010_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproducts',
            name='SNR_Category_Main',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
