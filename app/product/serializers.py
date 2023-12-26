from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'img1','img2' ,'img3','img4','category', 'name',
                  'description','price',
                  'manufacturer',
                  'created_at', 'updated_at']

        read_only_fields = ('created_at', 'updated_at')
