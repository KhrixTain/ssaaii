from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import  datetime

class Tipo_cuenta(models.Model):
   tipo = models.CharField(max_length=80, verbose_name='Tipo', unique=True)

   def __str__(self):
       return 'Nombre: {}'.format(self.nombre_cuenta)

   class Meta:
       verbose_name = 'Tipo_cuenta'
       verbose_name_plural = 'Tipo_cuentas'
       ordering = ['id']


class Cuentas(models.Model):


   nombre_cuentae = models.CharField(max_length=80, verbose_name='Nombre de Cuenta', unique=True)
   recibe_saldo = models.BooleanField(default=True)
   saldo_actual = models.FloatField()
   tipo_cuenta = models.ForeignKey(Tipo_cuenta, on_delete=models.CASCADE)
   cuenta_padre = models.ForeignKey('self', on_delete=models.CASCADE)


   def __str__(self):
       return 'Nombre: {}'.format(self.nombre_cuenta)


   class Meta:
       verbose_name = 'Cuenta'
       verbose_name_plural = 'Cuentas'
       ordering = ['id']




class Asientos(models.Model):


   fecha = models.DateField(default=datetime, verbose_name='Fecha_del_asiento')
   desctripcion = models.TextField(verbose_name='Descripcion')
   usuario = models.ForeignKey(User, on_delete=models.CASCADE)


   def __str__(self):
       return 'Nombre: {}'.format(self.nombre_cuenta)


   class Meta:
       verbose_name = 'asiento'
       verbose_name_plural = 'asientos'
       ordering = ['id']


class Cuenta_asientos(models.Model):

    DEBE = 'DB'
    HABER ='HB'
    choices = [
        (DEBE,'Debe'),
        (HABER,'Haber'),
    ]
    tipo = models.CharField(max_length=2, choices=choices, default=DEBE)
    id_cuenta = models.ForeignKey(Cuentas, on_delete=models.CASCADE)
    id_asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)
    monto = models.FloatField()

    saldo_parcial = models.FloatField()

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre_cuenta)

    class Meta:
        verbose_name = 'asiento'
        verbose_name_plural = 'asientos'
        ordering = ['id']

'''
Docuemntacion que explica  lo del tipo
https://docs.djangoproject.com/en/3.1/ref/models/fields/
'''

