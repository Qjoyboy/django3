from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc',)
    search_fields = ('name', 'desc',)
    list_filter = ('name', 'desc',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'price', 'create_date', 'last_change',)
    search_fields = ('name', 'desc',)
    list_filter = ('name', 'desc',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('prod', 'vers_num', 'vers_name')

