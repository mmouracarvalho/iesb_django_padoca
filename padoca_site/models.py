from django.db import models

class Produto(models.Model):
  nome = models.CharField(max_length=100)
  preco = models.DecimalField(max_digits=6, decimal_places=2)
  descricao = models.TextField()

class Pedido(models.Model):
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  criado_em = models.DateTimeField(auto_now_add=True)
  ativo = models.BooleanField(default=True)

class ItemPedido(models.Model):
  pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.PositiveIntegerField(default=1)