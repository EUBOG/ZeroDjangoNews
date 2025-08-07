# news/admin.py
from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('pub_date', 'author')
    search_fields = ('title', 'author')
    ordering = ('-pub_date',)  # сортировка: новые сверху