# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-13 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20170713_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cams',
            name='SNR_Available',
            field=models.CharField(default=' ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_Brand',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_Description',
            field=models.CharField(default=' ', max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_ImageURL',
            field=models.CharField(default=' ', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_ModelNo',
            field=models.CharField(default=' ', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_Price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_ProductURL',
            field=models.CharField(default=' ', max_length=2000),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_Title',
            field=models.CharField(default=' ', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cams',
            name='SNR_UPC',
            field=models.CharField(default=' ', max_length=500, null=True),
        ),
    ]
