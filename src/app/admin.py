from django.contrib import admin  # type: ignore
from .models import Category, Product, Order  # type: ignore


class ProductTabularInline(admin.TabularInline):
    model = Product


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE_HEADER'
    site_title = 'SITE_TITLE'
    index_title = 'INDEX_TITLE'
    empty_value_display = 'н/у'


appadmin = AppAdminSite(name='appadmin')


@admin.action(description='Опубликавать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Не публикавать')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'н/у'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Введите имя родительской категории и id категории'
    inlines = [ProductTabularInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'н/у'
    list_display = ('title', 'descr', 'article', 'category', 'price', 'count', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'заголовок/id/артикул/цена'
    fieldsets = (
        ('Основные настройки',
         {'fields': ('title', 'article', 'category', 'price'), 'description': 'Описание'}),
        ('Дополнительные настройки',
         {'fields': ('is_published', 'descr', 'count'), 'description': 'Описание'})
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'н/у'
    list_display = ('id', 'user', 'product', 'date_created', 'is_paid')
    list_filter = ('user', 'is_paid', 'product')
    search_fields = ('id', 'product')
    search_help_text = 'id/продукт'
    readonly_fields = ('date_created',)


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)
