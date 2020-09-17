from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.http import JsonResponse

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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        try:
            data=Cuentas.objects.get(uk=request.POST['nro_cuenta']).toJSON()
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupos = list()
        if (self.request.user.groups.filter(name='Contador').exists()):
            grupos.append("Contador")
        if (self.request.user.groups.filter(name='Gestor').exists()):
            grupos.append("Gestor")
        if (self.request.user.groups.filter(name='Empleado').exists()):
            grupos.append("Empleado")
        context['grupos'] = grupos
        return context

class LibroDiarioView(TemplateView):
    templatate_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }
