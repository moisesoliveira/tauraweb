from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.decorators import login_required

# Create your models here.


class Membro(AbstractUser):
    #    nome = models.CharField(max_length=250)
    #    email = models.EmailField()
#    matricula = models.PositiveIntegerField()
    area_de_atuacao = models.CharField(max_length=250)

    def __str__(self):
        return self.username