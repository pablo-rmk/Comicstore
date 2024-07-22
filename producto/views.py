from django.shortcuts import render
from django.shortcuts import get_object_or_404
from crud.models import Comic
import logging
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

logger = logging.getLogger(__name__)
# Create your views here.
def producto(request):
    comic_id = request.GET.get('id')
    logger.debug('comic_id: %s', comic_id)
    try:
        comic = Comic.objects.get(id=comic_id)
        context = {'comic': comic}
        return render(request, 'producto.html', context)
    except ObjectDoesNotExist:
        return redirect('/')