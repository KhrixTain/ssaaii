from django.db import models
class Empresa(models.Model):
    nombre = models.TextField(verbose_name='Nombre')
    cuit = models.TextField(verbose_name='CUIT',unique=True)
    razon_social = models.TextField(verbose_name='Razón Social')
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.TextField(verbose_name='Telefono')
    e_mail = models.TextField(verbose_name='e-mail')
    fecha_inicio_actividades = models.DateTimeField(null=True, editable=True, verbose_name='Fecha de inicio de Actividades')
    ingresos_brutos = models.TextField(default=cuit)

    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
# Create your models here.
