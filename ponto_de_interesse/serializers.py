from rest_framework import serializers
from .models import Ponto_interesse

class PontoInteresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto_interesse
        fields = ['id', 'nome', 'descricao', 'caminho_imagem', 'localizacao']
