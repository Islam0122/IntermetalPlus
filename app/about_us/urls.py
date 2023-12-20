from django.urls import path
from . import views

urlpatterns = [
    path('', views.About_UsViewSet.as_view({
        'get': 'list'
    }))]