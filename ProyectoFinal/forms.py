from django import forms
from .models import Disco

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['interprete', 'titulo', 'genero', 'año_lanzamiento', 'descripcion', 'imagen']
        widgets = {
            'año_lanzamiento': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }