from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Pais, Region, Comuna, Cliente
from django.views.decorators.csrf import csrf_exempt
from .forms import FormCliente


def registro(request):
    if(request.method == 'GET'):
        form = FormCliente()
        return render(request, 'registro.html', {'form': form })
    else:
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registro.html', {'form': FormCliente(), 'registro_exitoso': True})
        else:
            return render(request, 'registro.html', {'form': form})

def todos_los_paises(request):
    paises = Pais.objects.all()
    paises_list = list(paises.values('id_pais', 'nombre_pais'))  # Asumiendo que el modelo tiene estos campos
    return JsonResponse(paises_list, safe=False)

def regiones_por_pais(request, id_pais):
    regiones = Region.objects.filter(id_pais=id_pais)
    regiones_list = list(regiones.values('id_region', 'nombre_region'))  # Asumiendo que el modelo tiene estos campos
    return JsonResponse(regiones_list, safe=False)

def comunas_por_region(request, id_region):
    comunas = Comuna.objects.filter(id_region=id_region)
    comunas_list = list(comunas.values('id_comuna', 'nombre_comuna'))
    
    return JsonResponse(comunas_list, safe=False)

