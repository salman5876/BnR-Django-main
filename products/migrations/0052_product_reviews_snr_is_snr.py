# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-22 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_auto_20180222_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_reviews',
            name='SNR_IS_SNR',
            field=models.BooleanField(default=False),
        ),
    ]
