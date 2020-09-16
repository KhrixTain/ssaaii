from django.views.generic.list import ListView

from django.views.generic import TemplateView
from django import template
from homepage.models import *
from django.contrib.auth.models import Group, User

register = template.Library()

class MyHomePage(ListView):
    template_name = 'index.html'
    model = Cuenta_asientos
    context_object_name = 'cuenta_asientos'
    extra_context = {
        'title': "Página Principal",
    }

class LibroDiarioView(TemplateView):
    template_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }

