from django.views.generic import TemplateView
from django import template
from django.contrib.auth.models import Group

register = template.Library()

class MyHomePage(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': "Página Principal",
    }

class LibroDiarioView(TemplateView):
    template_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }
