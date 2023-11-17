from django import forms
from .models import Libro


class FormularioLibros(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["title", "author", "rating", "sinopsis"]
