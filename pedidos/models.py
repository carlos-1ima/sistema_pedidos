from django.db import models
from cardapio.models import Proteina

class Pedido(models.Model):
    TIPO_REFEICAO = [
        ('marmita_pequena', 'Marmita Pequena'),
        ('marmita_grande', 'Marmita Grande'),
        ('pf', 'Prato Feito'),
    ]
    
    cliente = models.CharField(max_length=100)
    proteinas = models.ManyToManyField(Proteina)
    tipo_refeicao = models.CharField(max_length=20, choices=TIPO_REFEICAO)
    observacao = models.TextField(blank=True)
    data = models.DateField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=20, choices=[('dinheiro', "Dinheiro"), ('pix', 'Pix'), ('cartao', 'Cartão')])
    entrega = models.CharField(max_length=20, choices=[('retirada', 'Retirada'), ('delivery', 'Delivery')])
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cliente} - {self.get_tipo_refeicao_display()}"
# Create your models here.
