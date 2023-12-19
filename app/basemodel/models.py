from django.db import models

from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        _('создано в: '),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _('обновленно в: '),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
