import json

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse
from homepage.forms import *
from django.views.generic import TemplateView, CreateView
from django import template
from homepage.models import *
from django.contrib.auth.models import Group, User

register = template.Library()



class LibroMayor(ListView):
    template_name = 'libroMayor.html'
    model = Cuenta_asientos
    extra_context = {
            'title': "Libro Mayor",
        }

class MyHomePage(CreateView):
    template_name = 'index.html'
    model = cuenta_asientoBorrador
    form_class = Cuenta_asientosForm#.cuenta.queryset = Cuentas.objects.filter(recibe_saldo=True, disponible=True)
    context_object_name = 'cuenta_asiento_borrador'
    success_url = reverse_lazy('homepage:index.html')

    extra_context = {
        'title': "Página Principal",
        'Cuentas':Cuentas.objects.all(),
        'Cuenta_Asientos':Cuenta_asientos.objects.all(),
        'Asientos':Asientos.objects.all(),
        'Cuenta_Asientos_Borrador': cuenta_asientoBorrador.objects.all(),
        'cuentaform':CuentaForm(),
        'cuentaAsientoForm': CuentaAsientoBorradorForm(),
    }
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        context = self.extra_context
        if (asientoBorrador.objects.filter(usuario=self.request.user.id).exists()):
            context['asientoBorrador'] = asientoBorrador.objects.get(usuario=self.request.user.id)
        else:
            a_b = asientoBorrador(usuario=User.objects.get(id=self.request.user.id))
            a_b.save()
            context['asientoBorrador'] = a_b
        return super().dispatch(request,args,*kwargs)

    def post(self,request,args,*kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'index.html':
                c = CuentaForm(request.POST)
                if c.is_valid():
                    c.save()
                else:
                   data=c.errors
            else:
                data['error']= 'No ha ingresado ningun campo'
        except Exception as e:
            data['error']=str(e)
        try:
            action = request.POST['action']
            if action == 'index.html':
                c_a = CuentaAsientoBorradorForm(request.POST)
                if c_a.is_valid():
                    c_a.save()
                else:
                   data=c_a.errors
            else:
                data['error']= 'No ha ingresado ningun campo'
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
        """Estas dos lineas de abajo son para que la vista createview muestre los datos tipo object del listado"""
        #kwargs['object_list'] = Cuenta_asientos.objects.all()
        context['object_list'] = Cuenta_asientos.objects.all()
        context['list_url'] = reverse_lazy('homepage:index.html')
        context['action'] = 'index.html'
        #return super(MyHomePage, self).get_context_data(**kwargs)
        return context

class LibroDiarioView(TemplateView):
    templatate_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }
class Main(TemplateView):
    template_name = 'main.html'
