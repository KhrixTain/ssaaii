from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Tipo_cuenta(models.Model):
   tipo = models.CharField(max_length=80, verbose_name='Tipo', unique=True)

   def __str__(self):
       return self.tipo

   class Meta:
       verbose_name = 'Tipo_cuenta'
       verbose_name_plural = 'Tipo_cuentas'
       ordering = ['id']


class Cuentas(models.Model):

    nro_cuenta = models.IntegerField(verbose_name='Número de Cuenta',unique=True)
    nombre_cuenta = models.CharField(max_length=80, verbose_name='Nombre de Cuenta', unique=True)
    recibe_saldo = models.BooleanField(default=True)
    tipo_cuenta = models.ForeignKey(Tipo_cuenta, on_delete=models.PROTECT)
    cuenta_padre = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    saldo_actual = models.FloatField(null=True, blank=True)

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


   def __str__(self):
       return self.desctripcion


   class Meta:
       verbose_name = 'asiento'
       verbose_name_plural = 'asientos'
       ordering = ['id']


class Cuenta_asientos(models.Model):

    DEBE = 'D'
    HABER ='H'
    choices = [
        (DEBE,'Debe'),
        (HABER,'Haber'),
    ]
    tipo = models.CharField(max_length=1, choices=choices, default=DEBE)
    id_cuenta = models.ForeignKey(Cuentas, on_delete=models.PROTECT)
    id_asiento = models.ForeignKey(Asientos, on_delete=models.PROTECT)
    monto = models.FloatField(null=True, blank=True)

    saldo_parcial = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'cuenta_asiento'
        verbose_name_plural = 'cuentas_asientos'
        ordering = ['id']

'''
Docuemntacion que explica  lo del tipo
https://docs.djangoproject.com/en/3.1/ref/models/fields/
'''

