from django.db import models  # type: ignore
from django.contrib.auth import get_user_model  # type: ignore

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название',
        help_text='макс. 24 символа'
    )
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='родительская категория'
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='макс. 140 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='опубликовано'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', 'is_published')


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='название',
        help_text='макс. 36 символов'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text='макс. 140 символов'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='артикль',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикации',
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text='9999.99'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='количество',
        help_text='количество товара на складе'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='категория',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price', 'title', 'article')


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='покупатель'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='товар'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания',
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="оплачено"
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'app_order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date_created', '-id')
