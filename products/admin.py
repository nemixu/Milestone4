from django.contrib import admin
from .models import Product, Category, Review

class ProductAdmin(admin.ModelAdmin):
    """
    Organising the list display names for easy reading for admin panel.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Admin created to display friendly name or a category and the name.
    """
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    """
    To display the below fields to the Review admin panel.
    """
    list_display = (
        'user',
        'comment',
        'product',
        'rating'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
