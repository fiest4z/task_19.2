from decimal import Decimal

from django.db import models

from users.models import User

BLANK_NULL_TRUE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**BLANK_NULL_TRUE, verbose_name="Описание")
    preview = models.ImageField(**BLANK_NULL_TRUE, verbose_name="Изображение")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"),
                                verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    owner = models.ForeignKey(User, verbose_name='Владелец товара', **BLANK_NULL_TRUE, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Может отменить публикацию продукта"),
            ("can_change_description", "Может изменить описание продукта"),
            ("can_change_category", "Может изменить категорию продукта"),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    is_active = models.BooleanField(default=False, verbose_name="Активность версии")

    def __str__(self):
        return f"{self.version_name} - ({self.version_number})"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
