# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_auto_20180504_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='SNR_isShow',
            field=models.BooleanField(default=True),
        ),
    ]
