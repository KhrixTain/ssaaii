from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, TemplateView
from customers.models import *
from articles.models import *
from sales.forms import VentaForm
from sales.models import *
##from sales.form import *

class VentasView(CreateView):
    template_name = 'CargarVenta.html'
    model = Ventas
    form_class = VentaForm
    success_url = reverse_lazy('sales:CargarVenta')
