from django.shortcuts import render, redirect
from .models import Comic
from .forms import FormComic
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def crud(request):
    return redirect('login')

def superuser_required(view_func):
    decorated_view = user_passes_test(
        lambda u: u.is_authenticated and u.is_superuser,
        login_url='landing:index',  
    )
    return decorated_view(view_func)

@superuser_required
def listar(request):
    comics = Comic.objects.all()
    context = { 'comics': comics }
    return render(request, 'listar.html', context)

@superuser_required
def crear(request):
    if request.method == "POST":
        form = FormComic(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = FormComic()
    return render(request, 'crear.html', {'form': form})

@superuser_required
def eliminar(request, id):
    comic = Comic.objects.get(id=id)
    if comic:
        comic.delete()
        return redirect('listar')
    else:
        message = "No se encontró el comic"
        return redirect('listar')

@superuser_required
def editar(request, id):
    comic = Comic.objects.get(id=id)
    if comic:
        if request.method == "POST":
            form = FormComic(request.POST, instance=comic)
            if form.is_valid():
                form.save()
                return redirect('listar')
        else:
            form = FormComic(instance=comic)
        return render(request, 'editar.html', {'form': form})

