from django.forms import ModelForm
from homepage.models import *

class CuentaForm(ModelForm):
    class Meta:
        model = Cuentas
        fields= '__all__'
