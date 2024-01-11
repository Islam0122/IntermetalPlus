from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'img1', 'img2', 'img3', 'img4', 'video', 'price', 'description', 'detail_description')
        read_only_fields = ('created_at', 'updated_at')
