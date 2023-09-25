from django.db import models

# Create your models here.
#Class ponto de interesse e atributos
class Ponto_interesse(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    caminho_imagem = models.ImageField(upload_to='ponto_de_interesse/')
    localizacao = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nome
    