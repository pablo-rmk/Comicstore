import os
import json
import django

# Define el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comicstore.settings')  # Reemplaza 'tu_proyecto' con el nombre de tu proyecto

# Configura Django
django.setup()

from registro.models import Region, Pais 

def run():
    with open('regiones.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for region_data in data:
        try:
            id_pais = Pais.objects.get(id_pais=region_data['pais_id']) 
        except Pais.DoesNotExist:
            print(f"Error: No se encontró el país con id_pais={region_data['pais_id']}")
            continue  # Saltar a la siguiente región si no se encuentra el país

        Region.objects.create(
            id_region=str(region_data['region_id']),  # Convertir a str si es necesario
            nombre_region=region_data['nombre'],
            id_pais=id_pais
        )

if __name__ == '__main__':
    run()