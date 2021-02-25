from django.forms import *
from sales.models import *

class VentaForm(ModelForm):
    class Meta:
        model=Ventas
        fields=(
        'transportista',
        'cobrador',
        'tipo_bonificacion',
        'codigo',
        'porcentaje_descuento',
        'descuento',
        'condicion_de_venta',
        'zona_fiscal',
        'entrega',
        'articulo',
        'cliente',
        'fecha',
        )
        widgets = {
            'fecha': DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date',
                    'placeholder': 'Ingrese fecha',
                    'autocomplete': 'off',
                }
            ),
            'codigo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese codigo',
                    'autocomplete': 'off',
                },
            )
        }
