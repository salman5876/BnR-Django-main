# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0070_auto_20181206_1348'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailydeals',
            unique_together=set([('SNR_Title', 'SNR_Available', 'SNR_PriceAfter')]),
        ),
    ]
