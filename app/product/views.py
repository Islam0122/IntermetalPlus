from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from app.basemodel.pagination import CustomPageNumberPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        base_queryset = Product.objects.all()
        # Поиск по имени: / api / products /?search = "name"
        search = self.request.query_params.get('search', None)
        if search:
            base_queryset = base_queryset.filter(Q(name__icontains=search))
        # Фильтрация по категории:/ api / products /?category ="category"
        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            base_queryset = base_queryset.filter(category__title__iexact=category_filter)

        return base_queryset
