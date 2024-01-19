from django.contrib import admin

from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'slug', 'preview', 'create_date', 'ispublished', 'view_count',)
    search_fields = ('title', 'slug')
