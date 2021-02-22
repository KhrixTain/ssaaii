from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from customers.models import *
from articles.models import *
from sales.models import *

class ABMarticlesview(CreateView):
    template_name = "ABMarticles.html"
    model = Articulos
    #preguntar esto
    fields = ['codigo_item']

# Create your views here.
