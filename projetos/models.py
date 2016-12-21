from django.db import models
from membros.models import Membro


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(max_length=3096)
    responsavel = models.ForeignKey(Membro, blank=True, null=True)
#    autor = models.ForeignKey(Membro, null=True, blank=True)
#    data_hora = models.DateTimeField(auto_now_add=True)
