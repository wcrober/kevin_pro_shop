from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self): # This will allow what is returned by the database is the default name of the product
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField(blank=True)
    gender = models.CharField(max_length=2, default='M')
    color = models.CharField(max_length=255, blank=True)
    hand = models.CharField(max_length=1, default='R')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_creator')

    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('-created',)


    def __str__(self):
        return self.name
