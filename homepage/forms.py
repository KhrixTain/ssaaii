from django.forms import ModelForm
from homepage.models import *

class CuentaForm(ModelForm):

    """def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['__all__'].widget.attrs[ 'autofocus']=True"""
    class Meta:
        model = Cuentas
        fields= '__all__'

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