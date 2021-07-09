from django import forms

from customers.models import Clientes, Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField( widget= forms.TextInput(attrs={'placeholder':'Nombre/s...'}), label=False)
    surname = forms.CharField( widget= forms.TextInput(attrs={'placeholder':'Apellido/s...'}), label=False)
    class Meta:
        model = Customer
        fields = ['name', 'surname']

