# Create your views here.
from rest_framework import generics, status
from .models import Ponto_interesse
from .serializers import PontoInteresseSerializer
import os
from rest_framework.response import Response


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