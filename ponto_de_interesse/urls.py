from django.urls import path
from .views import PontoInteresseListAPIView, PontoInteresseDetailAPIView

urlpatterns = [
    path('', PontoInteresseListAPIView.as_view(), name='ponto-interesse-list'),
    path('<int:pk>/', PontoInteresseDetailAPIView.as_view(), name='ponto-interesse-detail'),
]
