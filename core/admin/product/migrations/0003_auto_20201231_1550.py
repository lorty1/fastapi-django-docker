# Generated by Django 3.1.4 on 2020-12-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201230_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
