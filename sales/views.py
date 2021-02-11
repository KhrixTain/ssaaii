from django.shortcuts import render
from sales.forms import *
# Create your views here.
from django.views.generic import CreateView
from sales.models import *

class VentasView(CreateView):
    template_name = 'CargaVenta.html'
    model = Ventas
    form_class = VentaForm
    context_object_name = 'ventaForm'
    extra_context = {

    }