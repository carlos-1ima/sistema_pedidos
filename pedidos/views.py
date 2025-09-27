from django.shortcuts import render, redirect
from .forms import PedidoForm

def index(request):
    return render(request, 'pedidos/index.html')

def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/criar_pedido.html', {'form': form})

def lista_pedidos(request):
    from .models import Pedido
    pedidos = Pedido.objects.all().order_by('-data_criacao')
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

# Create your views here.
