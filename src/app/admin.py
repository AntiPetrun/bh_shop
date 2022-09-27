from django.contrib import admin  # type: ignore
from .models import Category, Product, Order  # type: ignore


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'н/у'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя родительской категории и id категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'н/у'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'заголовок/id/артикул/цена'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'н/у'
    list_display = ('id', 'user', 'product', 'date_created', 'is_paid')
    list_filter = ('user', 'is_paid', 'product')
    search_fields = ('id', 'product')
    search_help_text = 'id/продукт'
