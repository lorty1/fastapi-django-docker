# Generated by Django 3.1.4 on 2021-01-05 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_products_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
