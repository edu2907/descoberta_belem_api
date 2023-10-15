from django.urls import path
from .views import ComentarioAvaliacaoListAPIView, PontoInteresseListAPIView, PontoInteresseDetailAPIView

urlpatterns = [
    path('', PontoInteresseListAPIView.as_view(), name='ponto-interesse-list'),
    path('<int:pk>/', PontoInteresseDetailAPIView.as_view(), name='ponto-interesse-detail'),
    path('<int:pk>/comentarios/', ComentarioAvaliacaoListAPIView.as_view(), name='comentario-avaliacao-list')
]
