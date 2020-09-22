from django.forms import *
from homepage.models import *

class CuentaForm(ModelForm):

    """def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['__all__'].widget.attrs[ 'autofocus']=True"""
    class Meta:
        model = Cuentas
        fields= '__all__'
        widgets = {

        }
    """
    def save(self,commit=True):
        data= {}
        form=super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str(e)
        return data """

class Cuenta_asientosForm(ModelForm):

    class Meta:
        model = Cuenta_asientos
        fields='__all__'
        labels = {
            'id_cuenta': 'Cuenta',
            'id_asiento': 'Asiento'
        }
        widgets = {
            'tipo': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_cuenta': Select(
                attrs= {
                    'class' : 'form-control'
                }
            ),
            'id_asiento': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione asiento'
                }
            ),
            'monto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese monto',
                    'autocomplete': 'off'
                }
            ),
            'saldo_parcial': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese saldo parcial',
                    'autocomplete': 'off'
        }
            )

        }
