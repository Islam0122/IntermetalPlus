from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.conf import settings

from app.basemodel.models import BaseModel


# Function to generate the path for uploaded product images
def product_image_path(instance, filename):
    # Use the model name as a subdirectory within "Product_images" and include a timestamp
    return f'Product_images/{slugify(instance.name)}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


# Model for products
class Product(BaseModel):
    name = models.CharField(_('Название товора'), max_length=204)
    img1 = models.ImageField(_('Изображение 1'), upload_to=product_image_path)
    img2 = models.ImageField(_('Изображение 2'), upload_to=product_image_path)
    img3 = models.ImageField(_('Изображение 3'), upload_to=product_image_path)
    img4 = models.ImageField(_('Изображение 4'), upload_to=product_image_path)
    video = models.URLField(_('URL видео'))
    price = models.CharField(_('Цена'), max_length=200)
    description = models.TextField(_('Описание'))
    detail_description = models.TextField(_('Характеристики'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
