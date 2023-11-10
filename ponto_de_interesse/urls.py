from django.urls import path
from .views import ComentarioAvaliacaoListAPIView, PontoInteresseListAPIView, PontoInteresseDetailAPIView, UsuarioRepDetailAPIView

urlpatterns = [
    path('', PontoInteresseListAPIView.as_view(), name='ponto-interesse-list'),
    path('<int:pk>/', PontoInteresseDetailAPIView.as_view(), name='ponto-interesse-detail'),
    path('<int:pk>/comentarios/', ComentarioAvaliacaoListAPIView.as_view(), name='comentario-avaliacao-list'),
    path('<int:pk>/reputacao/', UsuarioRepDetailAPIView.as_view(), name='usuario-reputacao-detail'),
]
