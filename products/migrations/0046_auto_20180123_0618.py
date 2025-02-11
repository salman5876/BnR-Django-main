# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_auto_20180123_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='applinces',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applinces',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='applinces',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='arts',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='arts',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='audio',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='audio',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='cams',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cams',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='cams',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carselectronics',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carselectronics',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='carselectronics',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='computersoftware',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='computersoftware',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='computersoftware',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='electronicgadgets',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='electronicgadgets',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='electronicgadgets',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flowerandplants',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flowerandplants',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='furniture',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='furniture',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='healthandfitness',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='healthandfitness',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='healthandfitness',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homeandgarden',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homeandgarden',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='movies',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='officesupply',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='officesupply',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='officesupply',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='smarthomes',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='smarthomes',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='smarthomes',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sportinggoods',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sportinggoods',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='toys',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='toys',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='toys',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tv',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tv',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='tv',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='videogames',
            name='SNR_Condition',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='videogames',
            name='SNR_PriceBefore',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='videogames',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='arts',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flowerandplants',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='SNR_SubCategory',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True),
        ),
    ]
