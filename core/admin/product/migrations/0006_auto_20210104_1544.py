# Generated by Django 3.1.4 on 2021-01-04 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_products_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
