from django.db import models

from membros.models import Membro


class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    texto = models.TextField(max_length=3096)
#    autor = models.ForeignKey(Membro, null=True, blank=True)
#    data_hora = models.DateTimeField(auto_now_add=True)
