import json

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from homepage.forms import *
from django.views.generic import TemplateView, CreateView
from django import template
from homepage.models import *
from django.contrib.auth.models import Group, User

register = template.Library()



class LibroMayor(ListView):
    template_name = 'libroMayor.html'
    model = cuenta_asientoBorrador
    extra_context = {
            'title': "Libro Mayor",
        }

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
        # kwargs['object_list'] = Cuenta_asientos.objects.all()
        context['object_list'] = cuenta_asientoBorrador.objects.all()
        context['list_url'] = reverse_lazy('homepage:index.html')
        context['action'] = 'index.html'
        # return super(MyHomePage, self).get_context_data(**kwargs)
        return context





class MyHomePage(CreateView):
    template_name = 'index.html'
    model = cuenta_asientoBorrador
    form_class = Cuenta_asientosForm
    context_object_name = 'cuenta_asiento_borrador'
    success_url = reverse_lazy('homepage:index.html')

    extra_context = {
        'title': "Página Principal",
        'Cuentas':Cuentas.objects.all(),
        'Cuenta_Asientos':Cuenta_asientos.objects.all(),
        'Asientos':Asientos.objects.all(),
        'Cuenta_Asientos_Borrador': cuenta_asientoBorrador.objects.all(),
        'cuentaform':CuentaForm(),
        'asientoBorradorForm': AsientoBorradorForm(),
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
        context['object_list'] = cuenta_asientoBorrador.objects.all()
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

class CargarAsiento(TemplateView):
    template_name = "error_asiento.html"

    def dispatch(self, request, *args, **kwargs):
        errores = list()
        asiento = None
        if( asientoBorrador.objects.filter(usuario=request.user.id).exists() != True ):
            return redirect(reverse_lazy('homepage'))
        elif( cuenta_asientoBorrador.objects.filter(cuenta=asientoBorrador.objects.get(usuario=request.user.id).id).exists() ):
            asiento = asientoBorrador.objects.get(usuario=request.user.id)
            def asentar_asiento_borrador(asiento):
                nuevo_asiento = Asientos()
                nuevo_asiento.desctripcion = asiento.descripcion
                nuevo_asiento.fecha = asiento.fecha
                nuevo_asiento.usuario = asiento.usuario
                nuevo_asiento.save()
                for cuenta_asiento_borrador in cuenta_asientoBorrador.objects.filter(cuenta=asiento.cuenta.id):
                    nueva_cuenta_asiento = Cuenta_asientos()
                    nueva_cuenta_asiento.monto = cuenta_asiento_borrador.monto
                    nueva_cuenta_asiento.tipo = cuenta_asiento_borrador.tipo
                    nueva_cuenta_asiento.asiento = nuevo_asiento
                    nueva_cuenta_asiento.id_cuenta = cuenta_asiento_borrador.cuenta
                    nueva_cuenta_asiento.save()
            def analizar_monto_cuenta_asiento(c_a, errores):
                if( c_a.monto is not None and c_a.cuenta.saldo_actual is not None ):
                    if( c_a.cuenta.getTipoCuenta() in ["Activo"] and c_a.tipo == "H" and c_a.monto > Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual ):
                        mensaje = "La cuenta "+str(Cuentas.objects.get(id=c_a.cuenta.id).nombre_cuenta) + " posee de saldo " + str(Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual) + " y se trató de extraer " + str(c_a.monto) + "."
                        errores.append(mensaje)
                    elif(c_a.cuenta.getTipoCuenta in ["Pasivo"] and c_a.tipo == "D" and c_a.monto > Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual):
                        mensaje = "La cuenta " + str(Cuentas.objects.get(id=c_a.cuenta.id).nombre_cuenta) + " posee de saldo " + str(Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual) + " y se trató de extraer " + str(c_a.monto) + "."
                        errores.append(mensaje)
                return errores
            def analizar_doble_partida_asiento(asiento):
                debe = 0
                haber = 0
                for c_a in cuenta_asientoBorrador.objects.filter(asiento=asiento.id):
                    if ( c_a.tipo == "D" ):
                        debe = debe + c_a.monto
                    elif( c_a.tipo == "H" ):
                        haber = haber + c_a.monto
                return debe == haber
            asiento = asientoBorrador.objects.get(usuario=request.user.id)
            if( asiento.descripcion == "SIN_TITULO" ):
                errores.append("No se ha ingresado un título al asiento.")
            if( asiento.fecha is None ):
                errores.append("No se ha ingresado una fecha al asiento.")
            else:
                if( asiento.fecha > now ):
                    errores.append("La fecha ingresada no ha sucedido aún.")
                elif( asiento.fecha < Asientos.objects.all().order_by("-fecha").first().fecha):
                    errores.append("La fecha ingresada es muy antigüa.")
            for c_a in cuenta_asientoBorrador.objects.filter(asiento=asiento.id):
                errores = analizar_monto_cuenta_asiento(c_a, errores)
            if( analizar_doble_partida_asiento(asiento) == False ):
                errores.append("Los montos ingresados por el DEBE y el HABER son distintos")
            if (len(errores)==0 ):
                asentar_asiento_borrador(asiento)
                asiento.delete()
                return redirect(reverse_lazy('homepage'))
            else:
                contexto = super().get_context_data()
                asiento.delete()
                contexto['errores'] = errores
                return render(request=request, template_name=self.template_name, context=contexto)
        else:
            return redirect(reverse_lazy('homepage'))