# Generated by Django 3.1.4 on 2021-01-05 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210105_1006'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
