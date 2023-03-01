from django import forms
from hous3d.models import Modelo

class ModeloForm(forms.ModelForm):

    class Meta:
        model = Modelo
        fields = ['nombre', 'dimension', 'material', 'color', 'precio', 'descripcion']