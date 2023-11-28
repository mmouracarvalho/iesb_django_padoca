from django.urls import path, include
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('produtos/', include('nome_do_app.urls')),
  path('produto/adicionar/', views.adicionar_produto, name='adicionar_produto'),
  path('', views.lista_produtos, name='lista_produtos'),
  path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
  path('adicionar_ao_pedido/<int:produto_id>/', views.adicionar_ao_pedido, name='adicionar_ao_pedido')
]