from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        modelo = Pedido
        widgets = ['cliente', 'proteinas', 'observacao']
        widgets = {
            'proteinas': forms.CheckboxSelectMultiple(),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }