# Generated by Django 2.2 on 2019-10-24 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0112_auto_20191019_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebayindividualurls',
            name='soup',
        ),
    ]
