from django.shortcuts import render
from crud.models import Comic
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    comics_list = Comic.objects.all().order_by('id')
    paginator = Paginator(comics_list, 8)  # Muestra 8 cómics por página
    page_number = request.GET.get('page')
    comics = paginator.get_page(page_number)

    context = { 'comics': comics }
    return render(request, 'index.html', context)