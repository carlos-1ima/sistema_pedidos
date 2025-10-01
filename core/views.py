from django.shortcuts import redirect

def home(request):
    # redireciona a home diretamente para pedidos
    return redirect('index')
# Create your views here.
