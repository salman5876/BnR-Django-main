# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0058_categorymapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymapping',
            name='Cat_ID',
            field=models.IntegerField(null=True),
        ),
    ]
