from django.urls import path
from .views import PontoInteresseListAPIView

urlpatterns = [
    path('pontos-de-interesse/', PontoInteresseListAPIView.as_view(), name='ponto-interesse-list'),
]
