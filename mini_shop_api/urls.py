from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/categories/', CategoriesView.as_view()),
    path('api/v1/categories/<int:pk>', CategoryDetail.as_view()),
    path('api/v1/products/', ProductsView.as_view()),
    path('api/v1/products/<int:pk>', ProductDetail.as_view()),
    path('api/v1/customer/', CustomersView.as_view()),
    path('api/v1/cartproduct/', CartProduct.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)