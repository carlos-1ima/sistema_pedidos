from django.db import models

class Proteina(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

# Create your models here.
