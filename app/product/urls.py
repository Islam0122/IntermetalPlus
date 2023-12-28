from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('', views.ProductViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'})),
    path('recommendedproduct/', views.RecommendedProductsView.as_view({'get': 'list'})),
    path('recommendedproduct/<int:pk>/', views.RecommendedProductsView.as_view({'get': 'retrieve'})),
]
