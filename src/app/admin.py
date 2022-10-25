from django.contrib import admin
from .models import Category, Product, Order, Contact


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.action(description='Publish')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Not publish')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'н/у'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('name', 'id')
    search_help_text = 'Enter category or id of category to search'
    inlines = [ProductTabularInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'н/у'
    list_display = ('title', 'descr', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id')
    search_help_text = 'Enter title or product id for search results'
    fieldsets = (
        ('Main settings',
         {'fields': ('title', 'article', 'category', 'price'), 'description': 'Description'}),
        ('Additional settings',
         {'fields': ('is_published', 'descr', 'image'), 'description': 'Description'})
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'н/у'
    list_display = ('id', 'user', 'display_products', 'date_created', 'is_paid')
    list_filter = ('user', 'is_paid', 'products')
    search_fields = ('id', 'products')
    search_help_text = 'Enter order id or product for search results'
    readonly_fields = ('date_created',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_created')
    list_filter = ('name', 'email')
    date_hierarchy = 'date_created'


class ContactManager(ContactAdmin):
    readonly_fields = ('name', 'email', 'message', 'date_created')
