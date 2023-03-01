from django import forms
from hous3d.models import Reserva

class ReservaForm (forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente','modelo','fecha','cantidad']