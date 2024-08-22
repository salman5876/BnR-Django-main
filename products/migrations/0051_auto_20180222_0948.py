# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-22 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0050_auto_20180221_0614'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product_reviews',
            unique_together=set([('Product', 'SNR_Review_Title', 'SNR_Review_Author', 'SNR_Review_Body')]),
        ),
    ]
