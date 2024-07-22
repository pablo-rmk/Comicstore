from django.urls import path
from . import views


urlpatterns = [
    path('', views.registro, name='registro'),
    path('pais/', views.todos_los_paises, name='todos_los_paises'),
    path('region/<int:id_pais>/', views.regiones_por_pais, name='regiones_por_pais'),
    path('comuna/<int:id_region>/', views.comunas_por_region, name='comunas_por_region'),
   
]

