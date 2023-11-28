from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('pedido/', views.fazer_pedido, name='fazer_pedido'),
    path('pedido/confirmacao/', views.confirmacao_pedido, name='confirmacao_pedido')
]