# Generated by Django 2.2 on 2021-03-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0120_auto_20210329_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydeals',
            name='SNR_CategoryURL',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='dailydeals',
            name='SNR_PageURL',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
