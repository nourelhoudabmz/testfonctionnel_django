from django.contrib import admin
from userapp.models import Tag, Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category']
    fields = ['product_name', 'description', 'tags', 'category', 'image']
    list_filter = ['category', 'tags']
    search_fields = ['product_name']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
