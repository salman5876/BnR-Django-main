# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-28 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0080_amazonurls'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonProxies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Proxy', models.CharField(max_length=200, unique=True)),
                ('count', models.CharField(max_length=200)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
