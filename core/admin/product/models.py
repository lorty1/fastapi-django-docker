# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(blank=True,max_length=250, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name="Catégorie"
        verbose_name_plural="Catégories"


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(blank=True,max_length=250, null=True)
    description = models.CharField(blank=True,max_length=250, null=True)
    is_active = models.BooleanField(blank=True,max_length=250, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'product'
        verbose_name="Produit"
        verbose_name_plural="Produits"
