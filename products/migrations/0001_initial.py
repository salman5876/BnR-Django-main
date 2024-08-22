# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-14 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNR_SKU', models.CharField(default='', max_length=500)),
                ('SNR_Title', models.CharField(default=None, max_length=1000, null=True)),
                ('SNR_ModelNo', models.CharField(default=None, max_length=500, null=True)),
                ('SNR_Brand', models.CharField(default=None, max_length=200, null=True)),
                ('SNR_UPC', models.CharField(default=None, max_length=500, null=True)),
                ('SNR_Price', models.CharField(blank=True, default=None, max_length=50)),
                ('SNR_Available', models.CharField(default=None, max_length=50, null=True)),
                ('SNR_ProductURL', models.CharField(default='', max_length=2000)),
                ('SNR_ImageURL', models.CharField(default=None, max_length=2000, null=True)),
                ('SNR_Description', models.CharField(default=None, max_length=8000, null=True)),
                ('SNR_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tv',
            unique_together=set([('SNR_SKU', 'SNR_ProductURL', 'SNR_ImageURL')]),
        ),
    ]
