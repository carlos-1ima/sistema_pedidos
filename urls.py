from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site,urls),
    path('pedidos/', include('pedidos.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),  # inclui as URLs do app pedidos
]
