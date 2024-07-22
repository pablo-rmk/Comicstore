from django import forms
from .models import Comic

class FormComic(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'img_path', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'img_path': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'img_path': 'Ruta de la Imagen',
            'price': 'Precio',
        }

