# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-22 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userReviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviews',
            name='SNR_TitleReview',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
