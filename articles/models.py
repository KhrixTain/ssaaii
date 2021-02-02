from django.db import models

class Rubros(models.Model):
    nombre=models.TextField(unique=True, verbose_name='Nombre')
    codigo=models.IntegerField(unique=True, verbose_name="Código")
    subrubro=models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Rubro'
        verbose_name_plural = 'Rubros'

class Articulos(models.Model):
    codigo_item = models.IntegerField(verbose_name='Código Item',unique=True)
    precio = models.FloatField(verbose_name='Precio')
    existencia = models.FloatField(verbose_name='Existencia')
    item_suspendido = models.BooleanField(verbose_name= 'Item suspendido')
    motivo_suspension = models.TextField (verbose_name='Motivo suspension')
    deposito = models.IntegerField(verbose_name='Deposito')
    codigo_barra = models.IntegerField(verbose_name='Código de barras')
    observacion = models.TextField(verbose_name= 'Observaciones')
    nombre = models.TextField(verbose_name='Nombre')
    stock_comprometido=models.FloatField(verbose_name='Stock Comprometido')
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE)

    def __init__(self):
        global codigo_articulo
        self.codigo_item = codigo_articulo
        codigo_articulo += 1
    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
# Create your models here.
