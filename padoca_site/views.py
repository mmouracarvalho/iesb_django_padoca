from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
  produtos = Produto.objects.all()
  return render(request, 'templates/lista_produtos.html', {'produtos': produtos})

@login_required
def fazer_pedido(request):
    if request.method == "POST":
      novo_pedido = Pedido.objects.create(usuario=request.user)

      for key, value in request.POST.items():
        if key.startswith('produto_'):
          produto_id = key.split('_')[1]
          quantidade = request.POST.get(f'quantidade_{produto_id}', 1)
          produto = Produto.objects.get(id=produto_id)
          
          ItemPedido.objects.create(pedido=novo_pedido, produto=produto, quantidade=quantidade)

      return redirect('confirmacao_pedido')
    else:
      produtos = Produto.objects.all()
      return render(request, 'fazer_pedido.html', {'produtos': produtos})
    
def confirmacao_pedido(request):
  return render(request, 'templates/confirmacao_pedido.html')