from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'img1', 'img2', 'img3', 'img4', 'video', 'price', 'description', 'detail_description')
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Название продукта'] = representation.pop('name')
        representation['Изображение 1'] = representation.pop('img1')
        representation['Изображение 2'] = representation.pop('img2')
        representation['Изображение 3'] = representation.pop('img3')
        representation['Изображение 4'] = representation.pop('img4')
        representation['URL видео'] = representation.pop('video')
        representation['Цена'] = representation.pop('price')
        representation['Описание'] = representation.pop('description')
        representation['Характеристики'] = representation.pop('detail_description')
        return representation
