from django.db import models

codigo_articulo=1

class Rubros(models.Model):
    nombre=models.TextField(unique=True, verbose_name='Nombre')
    codigo=models.IntegerField(unique=True, verbose_name="Código")
    subrubro=models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    #esto dá una cadena de caracteres con lo que se quiere mostrar
    def __str__(self):
        return self.nombre

    def getNombre(self):
        return str(self.nombre)

    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Rubro'
        verbose_name_plural = 'Rubros'

class Articulos(models.Model):
    codigo_item = models.IntegerField(verbose_name='Código Item',unique=True)
    precio = models.FloatField(verbose_name='Precio', null=True)
    existencia = models.FloatField(verbose_name='Existencia', null=True)
    item_suspendido = models.BooleanField(verbose_name= 'Item suspendido', null=True, default=False)
    motivo_suspension = models.TextField (verbose_name='Motivo suspension', null=True)
    deposito = models.IntegerField(verbose_name='Deposito', null=True)
    codigo_barra = models.IntegerField(verbose_name='Código de barras', null=True)
    observacion = models.TextField(verbose_name= 'Observaciones', null=True)
    nombre = models.TextField(verbose_name='Nombre', null=True)
    stock_comprometido=models.FloatField(verbose_name='Stock Comprometido', null=True)
    rubro = models.ForeignKey(Rubros, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.nombre

    def getCodigoItem(self):
        return str(self.nombre)

    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
# Create your models here.
