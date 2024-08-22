# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 10:23
from __future__ import unicode_literals

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0055_auto_20180404_0623'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product_review_ai',
            name='SNR_Review_Info_gin',
        ),
        migrations.AddIndex(
            model_name='product_review_ai',
            index=django.contrib.postgres.indexes.GinIndex(fields=['SNR_Review_Info'], name='products_pr_SNR_Rev_589398_gin'),
        ),
    ]
