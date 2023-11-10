# Create your views here.
from django.forms import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ComentarioAvaliacao, Ponto_interesse, UsuarioRep
from .serializers import ComentarioAvaliacaoSerializer, PontoInteresseSerializer, UsuarioRepSerializer
import os
from ponto_de_interesse import serializers

class PontoInteresseListAPIView(generics.ListCreateAPIView):
    queryset = Ponto_interesse.objects.all()
    serializer_class = PontoInteresseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PontoInteresseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ponto_interesse.objects.all()
    serializer_class = PontoInteresseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.caminho_imagem.path 

        if os.path.exists(file_path):
            os.remove(file_path)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComentarioAvaliacaoListAPIView(generics.ListCreateAPIView):
    serializer_class = ComentarioAvaliacaoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        ponto_interesse_id = self.kwargs['pk']
        return ComentarioAvaliacao.objects.filter(ponto_interesse=ponto_interesse_id)

    def post(self, request, *args, **kwargs):
        try:
            resposta = super().post(request, *args, **kwargs)
            usuario = request.user
            usuario_rep = UsuarioRep.objects.get(usuario=usuario)
            usuario_rep.atualizar_reputacao()
            return resposta
        except ValidationError as e:
            return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)

class UsuarioRepDetailAPIView(generics.RetrieveAPIView):
    queryset = UsuarioRep.objects.all()
    serializer_class = UsuarioRepSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
