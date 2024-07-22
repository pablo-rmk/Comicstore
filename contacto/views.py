from django.shortcuts import render

# Create your views here.

def contacto(request):
    context = {}
    return render(request, 'contacto.html', context)