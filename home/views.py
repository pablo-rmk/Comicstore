from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def no_superusers_allowed(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return HttpResponseRedirect(reverse('landing:index'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

@no_superusers_allowed
@login_required(login_url='landing:index')
def home(request):
    context = {}
    return render(request, 'home.html', {})



