from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)

            if user.is_superuser:
                return redirect('listar')
            else:
                return redirect('landing:index')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})
