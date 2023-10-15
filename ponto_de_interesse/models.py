from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Ponto_interesse(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    caminho_imagem = models.ImageField(upload_to='ponto_de_interesse/')
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class ComentarioAvaliacao(models.Model):
    ponto_interesse = models.ForeignKey(Ponto_interesse, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    avaliacao = models.IntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"Avaliação de {self.ponto_interesse.nome} por {self.usuario.username}"
