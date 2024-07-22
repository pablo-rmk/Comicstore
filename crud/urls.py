from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud, name='crud'),
    path('listar/', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]