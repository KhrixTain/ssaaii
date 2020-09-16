from django.forms import ModelForm
from homepage.models import *

class Cuenta_AsientosForm(ModelForm):
    class Meta:
        model = Tipo_cuenta
        fields= '__all__'
