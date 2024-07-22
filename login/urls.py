from django.urls import path
from .views import login_view  # Asegúrate de importar tu vista personalizada

urlpatterns = [
    path('', login_view, name='login')  # Actualiza esta línea para usar tu vista personalizada
]