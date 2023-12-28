import os
from django.utils import timezone

from app.basemodel.models import BaseModel
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.conf import settings


class Category(BaseModel):
    title = models.CharField(_('Категория'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


# Модель для товаров
def product_image_path(instance, filename):
    # Upload to "Product_images/<name>/" using the current timestamp
    return f'Product_imgs/{instance.name}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


class Product(BaseModel):
    name = models.CharField(_('Наименование'), max_length=204)
    img1 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    img2 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    img3 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    img4 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    category = models.ManyToManyField(Category)
    description = models.TextField(_('Описание'), blank=True, null=True)
    # quantity = models.PositiveIntegerField(default=0)  # Количество товара
    price = models.CharField(_('Цена'), max_length=20)
    manufacturer = models.CharField(_('Производитель'), max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

# Модель для отзывов о товарах
# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связь с моделью Product
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с моделью User
#     text = models.TextField()
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг отзыва
#
#     def __str__(self):
#         return f"{self.product} - {self.user}"
