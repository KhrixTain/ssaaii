from django.forms import *
from homepage.models import *


class CuentaForm(ModelForm):

    """def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['__all__'].widget.attrs[ 'autofocus']=True"""
    class Meta:
        model = Cuentas
        fields = (
            'nro_cuenta',
            'nombre_cuenta',
            'recibe_saldo',
            'tipo_cuenta',
            'cuenta_padre',
            'saldo_actual',
            'disponible',
        )

        widgets = {

        }
    # def __init__(self):
    #     super(CuentaForm, self).__init__()
    #     self.fields['cuenta_padre'].queryset = Cuentas.objects.filter(disponible=True, recibe_saldo=False)

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
class AsientoBorradorForm(ModelForm):
    class Meta:
        model = asientoBorrador
        fields = '__all__'

class CuentaAsientoBorradorForm(ModelForm):
    class Meta:
        model = cuenta_asientoBorrador
        fields = (
            'asiento',
            'tipo',
            'cuenta',
            'monto',
        )
        widgets = {
            'asiento': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tipo': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cuenta': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'monto': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese monto',
                    'autocomplete': 'off',
                    'min': '0'
                }
            )
        }
#     def __init__(self):
#         super(CuentaAsientoBorradorForm, self).__init__()
#         self.fields['cuenta'].queryset = Cuentas.objects.filter(recibe_saldo=True, disponible=True)
# #comentario para pushear
    def clean(self):
        monto = self.cleaned_data.get('monto')
        cuenta = self.cleaned_data.get('cuenta')
        tipo = self.cleaned_data.get('tipo')
        if( tipo == 'D'):
            if( cuenta.getTipoCuenta() == 'Pasivo' ):
                if( cuenta.saldo < monto ):
                    raise forms.ValidationError("El monto ingresado excede lo disponible en la cuenta especificada.")
        else:
            if( cuenta.getTipoCuenta() == 'Activo'):
                if( cuenta.saldo < monto ):
                    raise forms.ValidationError("El monto ingresado excede lo disponible en la cuenta especificada.")


class AsientoForm(ModelForm):

    """def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['__all__'].widget.attrs[ 'autofocus']=True"""
    class Meta:
        model = Asientos
        fields= '__all__'
        widgets = {

        }

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
