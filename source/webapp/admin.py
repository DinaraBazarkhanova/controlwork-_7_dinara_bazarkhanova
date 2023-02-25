from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    list_filter = ['id', 'title', 'category']
    search_fields = ['title', 'price']
    fields = ['title', 'price', 'description', 'created_at']
    readonly_fields = ['id', 'created_at']


admin.site.register(Product, ProductAdmin)
