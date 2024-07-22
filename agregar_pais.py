import os
import django

# Configura el entorno para usar la configuración de tu proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comicstore.settings')
django.setup()

from registro.models import Pais

def agregar_pais(nombre_pais):
    pais = Pais(nombre_pais=nombre_pais)
    pais.save()
    print(f"País agregado: {pais.nombre_pais} con ID: {pais.id_pais}")

# Ejemplo de uso
if __name__ == '__main__':
    nombre_pais = 'Chile'  # Cambia esto por el nombre del país que deseas agregar
    agregar_pais(nombre_pais)