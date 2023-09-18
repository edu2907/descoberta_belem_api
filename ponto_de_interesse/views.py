from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Ponto_interesse
from .serializers import PontoInteresseSerializer

class PontoInteresseListAPIView(generics.ListAPIView):
    queryset = Ponto_interesse.objects.all()
    serializer_class = PontoInteresseSerializer