# Generated by Django 2.2 on 2019-10-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0113_remove_ebayindividualurls_soup'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebayindividualurls',
            name='soup',
            field=models.TextField(blank=True, null=True),
        ),
    ]
