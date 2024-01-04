from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/contact/', include("app.contact.urls")),
                  path('api/v1/products/', include("app.product.urls")),
              ] + urls_swagger
