from django import forms
from .models import Caracteristica

class CaracteristicaForm(forms.ModelForm):
    
    class Meta:
        model = Caracteristica
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción'}),
        }