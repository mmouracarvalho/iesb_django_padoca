from django.db import models
from django.conf import settings

class Produto(models.Model):
  nome = models.CharField(max_length=100)
  preco = models.DecimalField(max_digits=6, decimal_places=2)
  descricao = models.TextField()

  def __str__(self):
    return self.nome
  
class Pedido(models.Model):
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  criado_em = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)
  ativo = models.BooleanField(default=True)

  def __str__(self):
      return f'Pedido {self.id}'

class ItemPedido(models.Model):
  pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.PositiveIntegerField(default=1)

  def __str__(self):
      return f'{self.quantidade} de {self.produto.nome}'