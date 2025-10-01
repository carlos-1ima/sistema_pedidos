from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'tipo_refeicao', 'proteinas', 'observacao', 'forma_pagamento', 'entrega']
        widgets = {
            'proteinas': forms.CheckboxSelectMultiple(),
            'observacao': forms.Textarea(attrs={'rows': 3}),
            'tipo_refeicao': forms.RadioSelect(),  
        }

