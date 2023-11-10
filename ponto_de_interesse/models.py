from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class UsuarioRep(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    reputacao = models.FloatField(default=0.0)

    def atualizar_reputacao(self):
        comentarios_count = ComentarioAvaliacao.objects.filter(usuario=self.usuario).count()
        avaliacoes_count = ComentarioAvaliacao.objects.filter(usuario=self.usuario).exclude(avaliacao=10).count()

        if comentarios_count + avaliacoes_count > 0:
            reputacao_total = (avaliacoes_count + comentarios_count) / (comentarios_count + avaliacoes_count)
            self.reputacao = reputacao_total
            self.save()

@receiver(post_save, sender=ComentarioAvaliacao)
def atualizar_reputacao(sender, instance, **kwargs):
    instance.usuario.usuariorep.atualizar_reputacao()