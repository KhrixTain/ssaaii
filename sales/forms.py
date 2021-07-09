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
                }),
            'transportista': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese transportista',
                    'autocomplete': 'off',
                }),
            'cobrador': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cobrador',
                    'autocomplete': 'off',
                }),
            'tipo_bonificacion': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese tipo de bonificacion',
                    'autocomplete': 'off',
                }),
            'porcentaje_descuento': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese porcentaje de descuento',
                    'autocomplete': 'off',
                }),
            'tipo_bonificacion': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese tipo de bonificacion',
                    'autocomplete': 'off',
                }),
            'descuento': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descuento',
                    'autocomplete': 'off',
                }),
            'condicion_de_venta': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese condicion de venta',
                    'autocomplete': 'off',
                }),
            'zona_fiscal': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese zona fiscal',
                    'autocomplete': 'off',
                }),
            'condicion_de_venta': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese condicion_ de venta',
                    'autocomplete': 'off',
                }),
            'entrega': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese lugar de entrega',
                    'autocomplete': 'off',
                }),
            'articulo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese articulo',
                    'autocomplete': 'off',
                }),
            'cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cliente',
                    'autocomplete': 'off',
                }),

        }
