from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'text']
    list_filter = ['id', 'name', 'status', 'text']
    search_fields = ['name', 'status']
    fields = ['name', 'status', 'text', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
