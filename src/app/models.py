import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name=_('category name'),
        help_text=_('max length of category is 24 characters')
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('main category')
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name=_('description'),
        help_text=_('max length is 140 symbols')
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name=_('is published')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('name', 'is_published')


class Product(models.Model):
    article = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        verbose_name=_('product article'),
    )
    title = models.CharField(
        max_length=36,
        verbose_name=_('product title'),
        help_text=_('max length of product title is 36 characters')
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name=_('description'),
        help_text=_('max length of description is 140 characters')
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name=_('is published'),
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        default=0,
        verbose_name=_('price'),
        help_text=_('9999.99')
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name=_('related category'),
    )
    image = models.ImageField(
        upload_to='products',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_product'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('price', 'title', 'article')


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_('consumer')
    )
    products = models.ManyToManyField(
        'Product',
        related_name='products',
        verbose_name=_('product')
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created date'),
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name=_('is_published')
    )

    def display_products(self, product):
        return ', '.join(product.title for product in self.products.all())

    display_products.short_description = 'Products'

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'app_order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date_created', '-id')


class Contact(models.Model):
    name = models.CharField(
        max_length=32
    )
    email = models.EmailField(
        max_length=32
    )
    message = models.TextField(
        blank=True,
        max_length=255,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.email}'

    class Meta:
        db_table = 'app_contact'
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ('-date_created',)
