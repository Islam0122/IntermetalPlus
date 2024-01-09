from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'img1', 'img2', 'img3','video', 'name','model', 'manufacturer','serial_number',
                  'price',
                  'description', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
