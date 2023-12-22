from django.db import models

from app.basemodel.models import BaseModel


class ContactUsMessage(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    contact_phone = models.CharField(max_length=200, blank=True, verbose_name='Contact Phone')

    def __str__(self):
        return f"Message from {self.name}"
