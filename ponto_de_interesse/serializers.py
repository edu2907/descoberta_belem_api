from pyexpat import model
from rest_framework import serializers
from .models import ComentarioAvaliacao, Ponto_interesse, UsuarioRep

class PontoInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto_interesse
        fields = ['id', 'nome', 'descricao', 'caminho_imagem', 'localizacao']

class ComentarioAvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioAvaliacao
        fields = ['id', 'usuario', 'comentario', 'avaliacao']

class UsuarioRepSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRep
        fields = ['usuario', 'reputacao']
