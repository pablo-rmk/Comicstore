import os
import csv
import django

# Define el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comicstore.settings')

# Configura Django
django.setup()

from registro.models import Comuna, Region

def run():
    with open('comunas.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila si contiene encabezados

        for row in reader:
            id_comuna, id_region, nombre_comuna = row

            try:
                id_region = Region.objects.get(id_region=id_region)
            except Region.DoesNotExist:
                print(f"Error: No se encontró la región con id_region={id_region}")
                continue  # Saltar a la siguiente comuna si no se encuentra la región

            Comuna.objects.create(
                id_comuna=id_comuna,
                nombre_comuna=nombre_comuna,
                id_region=id_region
            )

if __name__ == '__main__':
    run()
