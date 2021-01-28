from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    reservado_por = models.IntegerField(null=True, blank=True)
    data_reserva = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return self.nome