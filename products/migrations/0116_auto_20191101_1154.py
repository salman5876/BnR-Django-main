# Generated by Django 2.2 on 2019-11-01 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0115_auto_20191029_0618'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='allproductscoupons',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='allproductscoupons_backup',
            unique_together=set(),
        ),
    ]
