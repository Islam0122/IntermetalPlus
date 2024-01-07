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


# Функция для генерации пути загружаемого изображения товара
def product_image_path(instance, filename):
    # Use the model name as a subdirectory within "Product_images" and include timestamp
    return f'Product_images/{instance.model.title}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'

# Модель для товаров
class Product(BaseModel):
    name = models.CharField(_('Наименование'), max_length=204)
    img1 = models.ImageField(_('Изображение 1'), upload_to=product_image_path)
    img2 = models.ImageField(_('Изображение 2'), upload_to=product_image_path)
    img3 = models.ImageField(_('Изображение 3'), upload_to=product_image_path)
    video = models.FileField(_('Видео'), upload_to=product_image_path)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, verbose_name=_('Модель'))
    serial_number = models.CharField(_('Серийный номер'), max_length=255, unique=True)
    description = models.TextField(_('Описание'))
    price = models.CharField(_('Цена'))
    manufacturer = models.CharField(_('Производитель'), max_length=100)
    material = models.CharField(_('Материал изделия'), max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    is_recommended = models.BooleanField(default=False, verbose_name=_('Рекомендуемый'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
