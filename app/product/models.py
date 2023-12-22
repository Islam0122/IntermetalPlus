from django.db import models
from django.utils.translation import gettext_lazy as _
from app.basemodel.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(BaseModel):
    img = models.ImageField(upload_to='Product_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=204)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
