from rest_framework import serializers
from .models import Product, Model


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    model = serializers.SlugRelatedField(slug_field='title', queryset=Model.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'img1', 'img2', 'img3','video', 'name','model', 'manufacturer','serial_number','material','price',
                  'description', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')
