from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/products/', include("app.product.urls")),
                  path('api/v1/about_us/', include("app.about_us.urls")),
              ] + urls_swagger
