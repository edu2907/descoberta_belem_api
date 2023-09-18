from django.db import models

# Create your models here.
class Ponto_interesse(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    caminho_imagem = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome