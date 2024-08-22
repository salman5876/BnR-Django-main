# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userReviews', '0010_auto_20171103_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorReviewsScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNR_ProductTitle', models.CharField(default='', max_length=1500)),
                ('SNR_VendorScoreAll', jsonfield.fields.JSONField(null=True)),
                ('SNR_Date', models.DateTimeField(auto_now_add=True)),
                ('SNR_ProductID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='userReviews.VendorReviews')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vendorreviewsscore',
            unique_together=set([('SNR_ProductID',)]),
        ),
    ]
