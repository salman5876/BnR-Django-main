# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0079_delete_amazonurls'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonURLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat', models.CharField(max_length=200)),
                ('SubCat', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=2000)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
