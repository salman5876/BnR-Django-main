# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_auto_20180206_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_reviews',
            name='SNR_Review_Body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product_reviews',
            name='SNR_Review_Down',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product_reviews',
            name='SNR_Review_Stars',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product_reviews',
            name='SNR_Review_UP',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
