# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-11 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0006_auto_20170908_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_db',
            name='SNR_ModelNo',
            field=models.CharField(db_index=True, default=' ', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mobile_db',
            name='SNR_Title',
            field=models.CharField(db_index=True, default=' ', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mobile_db',
            name='SNR_UPC',
            field=models.CharField(db_index=True, default=' ', max_length=500, null=True),
        ),
    ]
