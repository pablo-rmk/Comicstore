from django import forms
from django.core.exceptions import ValidationError
from registro.models import Cliente
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class FormLogin(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario:',
        widget=forms.TextInput(attrs={'class': 'form-control mt-3'}),
        max_length=150  
    )
    password = forms.CharField(
        label='Contraseña:',
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-3'})
    )

    User = get_user_model()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
    
        if not User.objects.filter(username=username).exists():
            raise ValidationError('El nombre de usuario no está registrado.')
    
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Las credenciales son incorrectas.')
    
        # if not Cliente.objects.filter(user=user).exists():
        #     raise ValidationError('No hay un cliente asociado a este usuario.')
    
        self.user = user

        return cleaned_data