# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_auto_20180227_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_review_ai',
            name='Product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.AllProducts'),
        ),
    ]
