# This file tells Django which Models to administrate via the admin page
from django.contrib import admin

from .models import Category, Product, Service

@admin.register(Category) # Registers the model with admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'gender', 'color', 'hand', 'slug', 'image', 'price', 'in_stock',
                    'created', 'updated']
    list_filter = ['in_stock', 'name']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'price', 'slug', 'created', 'updated']
    list_filter = ['name', 'price']
    list_editable = ['desc', 'price']
    prepopulated_fields = {'slug': ('name',)}
