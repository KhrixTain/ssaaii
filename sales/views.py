from django.shortcuts import render

from django.views.generic import CreateView, TemplateView
from customers.models import *
from articles.models import *
from sales.models import *
##from sales.form import *

class VentasView(CreateView):
    template_name = 'CargaVenta.html'
    model = Ventas
    ##form_class = VentaForm
    context_object_name = 'ventaForm'
    extra_context = {
    }


# Create your views here.






