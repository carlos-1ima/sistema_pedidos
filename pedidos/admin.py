from django.contrib import admin
from .models import Pedido

admin.site.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo_refeicao', 'data')
    list_filter = ('tipo_refeicao', 'proteinas', 'data')
    search_fields = ('cliente',)
    filter_vertical = ('proteinas',)
# Register your models here.
