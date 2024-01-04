from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Product, Model
from .serializers import ProductSerializer, ModelSerializer


class ModelsViewSet(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    lookup_field = 'pk'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        base_queryset = Product.objects.all()
        # Поиск по имени: / api / products /?search = "name"
        search = self.request.query_params.get('search', None)
        if search:
            base_queryset = base_queryset.filter(
                Q(name__icontains=search) |
                Q(model__name__icontains=search) |
                Q(manufacturer__icontains=search)
            )
        return base_queryset


class RecommendedProductsView(ModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.filter(is_recommended=True)
