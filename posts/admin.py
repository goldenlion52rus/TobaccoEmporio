from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Модель постов в админке."""

    list_display = ('name', 'description')
    list_filter = ("name",)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    """Модель категории в админке."""

    list_display = ('name', 'description')
    list_filter = ("name",)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
