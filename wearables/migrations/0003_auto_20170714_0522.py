# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 05:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wearables', '0002_auto_20170706_0621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wearable_db',
            unique_together=set([('SNR_SKU', 'SNR_ProductURL', 'SNR_Price')]),
        ),
    ]
