from django.contrib.auth.models import User
from django.db import models
from django.forms import model_to_dict
from django.utils.timezone import now
from django.core.exceptions import ValidationError
#from flask_security.utils import _


class Tipo_cuenta(models.Model):
    tipo = models.CharField(max_length=80, verbose_name='Tipo', unique=True)

    def __str__(self):
        return self.tipo
    def getNombreTipoCuenta(self):
        return str(self.tipo)
    class Meta:
        verbose_name = 'Tipo_cuenta'
        verbose_name_plural = 'Tipo_cuentas'
        ordering = ['id']


class Cuentas(models.Model):
    nro_cuenta = models.IntegerField(verbose_name='Número de Cuenta', unique=True)
    nombre_cuenta = models.CharField(max_length=80, verbose_name='Nombre de Cuenta', unique=True)
    recibe_saldo = models.BooleanField(default=True)
    tipo_cuenta = models.ForeignKey(Tipo_cuenta, on_delete=models.PROTECT)
    cuenta_padre = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    saldo_actual = models.FloatField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def getTipoCuenta(self):
        return self.tipo_cuenta.getNombreTipoCuenta()
    def __str__(self):
        return self.nombre_cuenta

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['id']


class Asientos(models.Model):
    fecha = models.DateTimeField(default=now, editable=True, verbose_name='Fecha_del_asiento')
    desctripcion = models.TextField(verbose_name='Descripcion', editable=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def clean_field(self):
        debe=0
        haber=0
        cuenta_asientos = Cuenta_asientos.objects.filter(id_asiento=self.id)
        for c_a in cuenta_asientos:
            if c_a.tipo == 'D':
                debe = debe + c_a.monto
            else:
                haber = haber + c_a.monto
        if debe != haber:
            raise ValidationError(_('f'))

    def __str__(self):
        return self.desctripcion

    class Meta:
        verbose_name = 'asiento'
        verbose_name_plural = 'asientos'
        ordering = ['id']


class Cuenta_asientos(models.Model):
    DEBE = 'D'
    HABER = 'H'
    choices = [
        (DEBE, 'Debe'),
        (HABER, 'Haber'),
    ]
    tipo = models.CharField(max_length=1, choices=choices, default=DEBE)
    id_cuenta = models.ForeignKey(Cuentas, on_delete=models.PROTECT)
    id_asiento = models.ForeignKey(Asientos, on_delete=models.PROTECT)
    monto = models.FloatField(null=True, blank=True)

    saldo_parcial = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.tipo

    def toJson(self):
        item = model_to_dict(self)
        return item

class asientoBorrador(models.Model):
    fecha = models.DateTimeField(null=True, editable=True, verbose_name='Fecha_del_asiento')
    descripcion = models.CharField(default="SIN_NOMBRE", max_length=255, verbose_name='Descripcion', editable=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.descripcion

class cuenta_asientoBorrador(models.Model):
    DEBE = 'D'
    HABER = 'H'
    choices = [
        (DEBE, 'Debe'),
        (HABER, 'Haber'),
    ]
    tipo = models.CharField(max_length=1, choices=choices, default=DEBE)
    cuenta = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    asiento = models.ForeignKey(asientoBorrador, on_delete=models.CASCADE)
    monto = models.FloatField(null=False)


    '''
    def clean_field(self):

        if self.monto < 0:
            raise ValidationError(_('Se ha ingresado un motno negativo, por favor revise antes de concretar'))

    def clean(self):

        if self.tipo == 'H' and self.id_cuenta.tipo_cuenta.tipo == 'Activo' and self.monto > self.id_cuenta.saldo_actual:
            raise ValidationError(_('El monto ingresado supera al saldo de la cuenta Activo '))
        elif self.tipo == 'D' and self.id_cuenta.tipo_cuenta.tipo == 'Pasivo' and self.monto > self.id_cuenta.saldo_actual:
            raise ValidationError(_('El monto ingresado supera al saldo de la cuenta Pasivo'))

        ''''''
            Esperando respuesta del lean o del fer
            elif self.tipo == 'D' and self.id_cuenta.tipo_cuenta.tipo == 'Patrimonio' and self.monto > self.id_cuenta.saldo_actual:
            raise ValidationError(_('El monto ingresado supera al saldo de la cuenta Pasivo'))
            elif self.tipo == 'D' and self.id_cuenta.tipo_cuenta.tipo == 'Resultado (+)' and self.monto > self.id_cuenta.saldo_actual:
            raise ValidationError(_('El monto ingresado supera al saldo de la cuenta Pasivo'))
            NO SABEMO una wea
            
            ''''''

    def save(self, *args, **kwargs):
        if self.tipo == 'H' and self.id_cuenta.tipo_cuenta.tipo == 'Activo':
            self.id_cuenta.saldo_actual = self.id_cuenta.saldo_actual - self.monto
            self.id_cuenta.save()
        elif self.tipo == 'D' and self.id_cuenta.tipo_cuenta.tipo == 'Activo':
            self.id_cuenta.saldo_actual = self.id_cuenta.saldo_actual + self.monto
            self.id_cuenta.save()
        elif self.tipo == 'H' and self.id_cuenta.tipo_cuenta.tipo == 'Pasivo':
            self.id_cuenta.saldo_actual = self.id_cuenta.saldo_actual + self.monto
            self.id_cuenta.save()
        elif self.tipo == 'D' and self.id_cuenta.tipo_cuenta.tipo == 'Pasivo':
            self.id_cuenta.saldo_actual = self.id_cuenta.saldo_actual - self.monto
            self.id_cuenta.save()
        self.saldo_parcial=self.id_cuenta.saldo_actual
        super().save(*args, **kwargs)

    '''



    class Meta:
        verbose_name = 'cuenta_asiento'
        verbose_name_plural = 'cuentas_asientos'
        ordering = ['id']


'''
Docuemntacion que explica  lo del tipo
https://docs.djangoproject.com/en/3.1/ref/models/fields/
'''
