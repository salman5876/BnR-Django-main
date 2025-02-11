# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-11 10:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNR_ProductTitle', models.CharField(default=' ', max_length=500, null=True)),
                ('SNR_ProductURL', models.CharField(default=' ', max_length=100, null=True)),
                ('SNR_Price', models.DecimalField(blank=True, decimal_places=2, max_digits=50)),
                ('SNR_Date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
