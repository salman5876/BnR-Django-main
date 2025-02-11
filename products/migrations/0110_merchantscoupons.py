# Generated by Django 2.2 on 2019-10-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0109_auto_20191011_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='merchantscoupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('image20px', models.CharField(max_length=255, null=True)),
                ('image40px', models.CharField(max_length=255, null=True)),
                ('image60px', models.CharField(max_length=255, null=True)),
                ('image80px', models.CharField(max_length=255, null=True)),
                ('image100px', models.CharField(max_length=255, null=True)),
                ('prefer', models.IntegerField(blank=True, default=100, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
