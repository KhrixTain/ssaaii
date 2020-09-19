from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.http import JsonResponse
from homepage.forms import *
from django.views.generic import TemplateView, CreateView
from django import template
from homepage.models import *
from django.contrib.auth.models import Group, User

register = template.Library()

class MyHomePage(CreateView):
    template_name = 'index.html'
    model = Cuenta_asientos
    form_class=CuentaForm
    context_object_name = 'cuenta_asientos'
    success_url = reverse_lazy('homepage:index')
    extra_context = {
        'title': "Página Principal",
        'Cuentas':Cuentas.objects.all(),
        'Cuenta_Asientos':Cuenta_asientos.objects.all(),
        'Asientos':Asientos.objects.all()
    }
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data=form.errors
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
        context['action'] = 'add'
        #return super(MyHomePage, self).get_context_data(**kwargs)
        return context

class LibroDiarioView(TemplateView):
    templatate_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }
