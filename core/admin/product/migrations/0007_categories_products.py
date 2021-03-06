# Generated by Django 3.1.4 on 2021-01-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_auto_20210104_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
                'db_table': 'categories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('test', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'db_table': 'products',
                'managed': True,
            },
        ),
    ]
