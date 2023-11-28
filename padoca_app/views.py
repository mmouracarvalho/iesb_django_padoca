from django.core.paginator import Paginator
from .models import Produto, Pedido, ItemPedido
from .forms import ProdutoForm

def lista_produtos(request):
  produtos_lista = Produto.objects.all()
  paginator = Paginator(produtos_lista, 10) #10 produtos por página
  page = request.GET.get('page')
  produtos = paginator.get_page(page)
  return render(request, 'templates/lista_produtos.html', {'produtos': produtos})

def lista_pedidos(request):
  pedidos = Pedido.objects.filter(usuario=request.user, ativo=True)
  return render(request, 'templates/lista_pedidos.html', {'pedidos': pedidos})
  
def adicionar_ao_pedido(request, produto_id):
  produto = Produto.objects.get(id=produto_id)
  pedido, criado = Pedido.objects.get_or_create(usuario=request.user, ativo=True)
  item_pedido, criado = ItemPedido.objects.get_or_create(pedido=pedido, produto=produto)

  if not criado:
      item_pedido.quantidade += 1
      item_pedido.save()

  return redirect('lista_produtos')

def adicionar_produto(request):
  if request.method == 'POST':
    form = ProdutoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('lista_produtos')
  else:
      form = ProdutoForm()
  return render(request, 'templates/adicionar_produto.html', {'form': form})