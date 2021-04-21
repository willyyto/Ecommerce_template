from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
# Admin configuration for category model
class CategoryAdmin(admin.ModelAdmin):
    # Display name and slug on list
    list_display = ['name', 'slug']
    # Automatically write into the slug field when name is written
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock',
                    'is_active', 'created', 'updated']   
    # Add filtering based on fields   
    list_filter = ['in_stock', 'is_active' ]
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title', )}


