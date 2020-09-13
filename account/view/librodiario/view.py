'''from django.shortcuts import render
from django.http import HttpResponse

def librodiario_list(request):
    data = {

    }
    return HttpResponse(request, "templates/libro_diario_view.html",data)
'''
from django.views.generic import TemplateView

class LibroDiarioView(TemplateView):
    template_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }