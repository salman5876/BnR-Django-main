# Generated by Django 2.2 on 2019-08-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0096_auto_20190801_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebayindividualurls',
            name='status_error',
            field=models.BooleanField(default=False),
        ),
    ]
