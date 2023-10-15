# Create your views here.
from django.forms import ValidationError
from rest_framework import generics, status
from .models import ComentarioAvaliacao, Ponto_interesse
from .serializers import ComentarioAvaliacaoSerializer, PontoInteresseSerializer
import os
from rest_framework.response import Response

from ponto_de_interesse import serializers


class PontoInteresseListAPIView(generics.ListCreateAPIView):
    queryset = Ponto_interesse.objects.all()
    serializer_class = PontoInteresseSerializer

class PontoInteresseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ponto_interesse.objects.all()
    serializer_class = PontoInteresseSerializer

    def destroy(self, request, *args, **kwargs):
     # Clear images from storage
     instance = self.get_object()
     file_path = instance.caminho_imagem.path 
     
     if os.path.exists(file_path):
         os.remove(file_path)
         
     instance.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
    
class ComentarioAvaliacaoListAPIView(generics.ListCreateAPIView):
    serializer_class = ComentarioAvaliacaoSerializer

    def get_queryset(self):
        ponto_interesse_id = self.kwargs['pk']
        return ComentarioAvaliacao.objects.filter(ponto_interesse=ponto_interesse_id)
    
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as e:
            return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)

    
    def perform_create(self, serializer):
        ponto_interesse_id = self.kwargs['pk']
        try:
            ponto_interesse = Ponto_interesse.objects.get(pk=ponto_interesse_id)
            serializer.save(ponto_interesse=ponto_interesse)

        except Ponto_interesse.DoesNotExist:
            raise ValidationError({"ponto_interesse": "Ponto de interesse não existe."})