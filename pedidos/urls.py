from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # página inicial
    path('novo/', views.criar_pedido, name='criar_pedido'),
    path('lista/', views.lista_pedidos, name='lista_pedidos'),
]