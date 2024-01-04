import os
from django.utils import timezone

from app.basemodel.models import BaseModel
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.conf import settings


# Модель для товаров
class Model(BaseModel):
    title = models.CharField(_('Наименование модели'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Модель')
        verbose_name_plural = _('Модели')


# img -> file
def product_image_path(instance, filename):
    # Upload to "Product_images/<name>/" using the current timestamp
    return f'Product_imgs/{instance.name}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


# Модель для товаров
class Product(BaseModel):
    name = models.CharField(_('Наименование'), max_length=204)
    img1 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    img2 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    img3 = models.ImageField(_('Изображение'), upload_to=product_image_path, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, verbose_name=_('Модель'))
    description = models.TextField(_('Описание'), blank=True, null=True)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    manufacturer = models.CharField(_('Производитель'), max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
