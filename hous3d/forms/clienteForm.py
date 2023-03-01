from django import forms
from hous3d.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento', 'email', 'telefono', 'direccion']