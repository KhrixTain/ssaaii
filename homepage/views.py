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
from django.utils.datastructures import MultiValueDictKeyError

register = template.Library()

class ABMclientes(TemplateView):
    template_name = "ABMclientes.html"
class CargaVenta(TemplateView):
    template_name = "CargaVenta.html"

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
        context['Cuenta_asientoList'] = Cuenta_asientos.objects.all()
        context['list_url'] = reverse_lazy('homepage:index.html')
        context['action'] = 'index.html'
        # return super(MyHomePage, self).get_context_data(**kwargs)
        return context





class MyHomePage(CreateView):
    template_name = 'index.html'
    model = cuenta_asientoBorrador
    form_class = Cuenta_asientosForm
    context_object_name = 'cuenta_asiento_borrador'

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
                    c = c_a.instance
                    id_a= asientoBorrador.objects.get(usuario=request.user.id)
                    c.asiento = id_a
                    c.save()
                else:
                   data=c_a.errors
            else:
                data['error']= 'No ha ingresado ningun campo'
        except Exception as e:
            data['error']=str(e)
        try:
            action = request.POST['action']
            if action == 'index.html':
                a_f = AsientoBorradorForm(request.POST)
                if a_f.is_valid():
                    a_f_instance = a_f.instance
                    asiento= asientoBorrador.objects.get(usuario=request.user.id)
                    asiento.descripcion = a_f_instance.descripcion
                    asiento.fecha = a_f_instance.fecha
                    asiento.save()
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
        #kwargs['object_list'] = Cuenta_asientos.objects.all()aa
        context['object_list'] = Cuenta_asientos.objects.all()
        context['Cuentas'] = Cuentas.objects.all()
        context['list_url'] = reverse_lazy('homepage:index.html')
        context['action'] = 'index.html'
        return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = ''
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
        asiento=asientoBorrador.objects.get(usuario=request.user.id)
        if( asientoBorrador.objects.filter(usuario=request.user.id).exists() != True ):
            return redirect(reverse_lazy('homepage:homepage'))
        elif( cuenta_asientoBorrador.objects.filter(asiento=asiento).exists() ):

            def asentar_asiento_borrador(asiento):
                nuevo_asiento = Asientos()
                nuevo_asiento.desctripcion = asiento.descripcion
                nuevo_asiento.fecha = asiento.fecha
                nuevo_asiento.usuario = asiento.usuario
                nuevo_asiento.save()

                for cuenta_asiento_borrador in cuenta_asientoBorrador.objects.filter(asiento=asiento):
                    nueva_cuenta_asiento = Cuenta_asientos()
                    nueva_cuenta_asiento.monto = cuenta_asiento_borrador.monto
                    cuenta = cuenta_asiento_borrador.cuenta
                    if (cuenta_asiento_borrador.cuenta.getTipoCuenta() in ["Activo","Resultado (+)"]):
                        if( cuenta_asiento_borrador.tipo == "D" ):
                            cuenta.saldo_actual = cuenta.saldo_actual + cuenta_asiento_borrador.monto
                        elif( cuenta_asiento_borrador.tipo == "H" ):
                            cuenta.saldo_actual = cuenta.saldo_actual - cuenta_asiento_borrador.monto
                    elif (cuenta_asiento_borrador.cuenta.getTipoCuenta() in ["Pasivo", "Resultado (-)","Patrimonio"]):
                        if (cuenta_asiento_borrador.tipo == "D"):
                            cuenta.saldo_actual = cuenta.saldo_actual - cuenta_asiento_borrador.monto
                        elif (cuenta_asiento_borrador.tipo == "H"):
                            cuenta.saldo_actual = cuenta.saldo_actual + cuenta_asiento_borrador.monto
                    cuenta.save()
                    nueva_cuenta_asiento.tipo = cuenta_asiento_borrador.tipo
                    nueva_cuenta_asiento.id_asiento = nuevo_asiento
                    nueva_cuenta_asiento.id_cuenta = cuenta_asiento_borrador.cuenta
                    nueva_cuenta_asiento.saldo_parcial = cuenta.saldo_actual
                    nueva_cuenta_asiento.save()
            def analizar_monto_cuenta_asiento(c_a, errores):
                if( c_a.monto is not None and c_a.cuenta.saldo_actual is not None ):
                    if( c_a.cuenta.getTipoCuenta() in ["Activo","Resultado (+)"] and c_a.tipo == "H" and c_a.monto > Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual ):
                        mensaje = "La cuenta "+str(Cuentas.objects.get(id=c_a.cuenta.id).nombre_cuenta) + " posee de saldo " + str(Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual) + " y se trató de extraer " + str(c_a.monto) + "."
                        errores.append(mensaje)
                    elif(c_a.cuenta.getTipoCuenta in ["Pasivo","Resultado (-)","Patrimonio"] and c_a.tipo == "D" and c_a.monto > Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual):
                        mensaje = "La cuenta " + str(Cuentas.objects.get(id=c_a.cuenta.id).nombre_cuenta) + " posee de saldo " + str(Cuentas.objects.get(id=c_a.cuenta.id).saldo_actual) + " y se trató de extraer " + str(c_a.monto) + "."
                        errores.append(mensaje)
                elif( c_a.monto is None ):
                    mensaje = "No se ha ingresado un monto para actualizar la cuenta "+ str(Cuentas.objects.get(id=c_a.cuenta).nombre_cuenta)
                    errores.append(mensaje)
                return errores
            def analizar_doble_partida_asiento(asiento):
                debe = 0
                haber = 0
                for c_a in cuenta_asientoBorrador.objects.filter(asiento=asiento):
                    if ( c_a.tipo == "D" ):
                        debe = debe + c_a.monto
                    elif( c_a.tipo == "H" ):
                        haber = haber + c_a.monto
                return debe == haber
            def analizar_unicidad_cuentas(asiento, errores):
                cuentas = set()
                for c_a in cuenta_asientoBorrador.objects.filter(asiento=asiento):
                    if( c_a.cuenta in cuentas):
                        mensaje = "La cuenta "+ str(c_a.cuenta.nombre_cuenta) +" se ha ingresado más de una vez."
                        errores.append(mensaje)
                    else:
                        cuentas.add(c_a.cuenta)
                return errores
            asiento = asientoBorrador.objects.get(usuario=request.user.id)
            if( asiento.descripcion == "SIN_NOMBRE" ):
                errores.append("No se ha ingresado un título al asiento.")
            # if( asiento ):
            #     if( asiento.fecha > now() ):
            #         errores.append("La fecha ingresada ha un no ha sucedido.")
            #     elif(asiento.fecha < Asientos.objects.all().order_by("-fecha").first().fecha ):
            #         errores.append("La fecha ingresada es muy antigüa.")
            # else:
            #     errores.append("No se ha ingresado una fecha.")
            errores = analizar_unicidad_cuentas(asiento,errores)
            for c_a in cuenta_asientoBorrador.objects.filter(asiento=asiento):
                errores = analizar_monto_cuenta_asiento(c_a, errores)
            if( analizar_doble_partida_asiento(asiento) == False ):
                errores.append("Los montos ingresados por el DEBE y el HABER son distintos.")
            if ( len(errores)==0 ):
                asentar_asiento_borrador(asiento)
                asiento.delete()
                return redirect(reverse_lazy('homepage:homepage'))
            else:
                contexto = super().get_context_data()
                asiento.delete()
                contexto['errores'] = errores
                return render(request=request, template_name=self.template_name, context=contexto)
        else:
            print("conejo")
            asiento.delete()
            return redirect(reverse_lazy('homepage:homepage'))