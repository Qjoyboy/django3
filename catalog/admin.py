from django.contrib import admin
from catalog.models import Product, Category, Blog


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

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug','body','preview','create_date','ispublished','view_count',)
    search_fields = ('title','slug')