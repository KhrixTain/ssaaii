from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, TemplateView, ListView, DetailView
from customers.models import *
from articles.models import *
from sales.forms import VentaForm
from sales.models import *
##from sales.form import *

class VentasView(CreateView):
    template_name = 'CargarVenta.html'
    model = Ventas
    form_class = VentaForm
    success_url = reverse_lazy('sales:resumenVenta')

class resumenVenta(CreateView):
    template_name= 'resumenVenta.html'
    model= Ventas
    fields = '__all__'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    extra_context = {
        'object_list':Ventas.objects.all()
    }
