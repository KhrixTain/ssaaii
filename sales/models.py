from django.db import models

# Create your models here.
from ssaaii.articles.models import Articulos
from ssaaii.company.models import Empresa
from ssaaii.customers.models import Clientes
##
codigo_cliente=1
codigo_articulo=1
codigo_venta=1
codigo_factura = 1

# Create your models here.

class Vendedores(models.Model):
    nombre = models.TextField(verbose_name='Nombre')
    dni = models.TextField(verbose_name='DNI',unique=True)
    codigo = models.TextField(verbose_name='Vendedor')
    fecha_de_ingreso=models.DateTimeField(null=True, editable=True, verbose_name='Fecha de Ingreso')

    class Meta:
        ordering= ["nombre"]
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Ventas(models.Model):
    CONTADO = 'C'
    TARJETA_CREDITO = 'T'
    FINANCIACION = 'F'
    CHEQUE = 'H'
    choices = [
        (CONTADO, 'Contado'),
        (TARJETA_CREDITO, 'Tarjeta_credito'),
        (FINANCIACION, 'Financiacion'),
        (CHEQUE, 'Cheque')
    ]
    transportista = models.TextField(verbose_name='Transportista')
    cobrador = models.TextField(verbose_name='Cobrador')
    tipo_bonificacion = models.FloatField(verbose_name='Tipo de bonificación')
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    porcentaje_descuento = models.FloatField(verbose_name='Porcentaje de Descuento')
    descuento = models.FloatField(verbose_name='Descuento')
    condicion_de_venta = models.CharField(max_length=1, choices=choices, verbose_name='Condición de Venta', unique=False, null=False)
    zona_fiscal = models.IntegerField(verbose_name='Zona fiscal')
    entrega = models.TextField(verbose_name='Entrega')
    articulo = models.ManyToManyField(Articulos)
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)

    def __init__(self):
        global codigo_venta
        self.codigo = codigo_venta
        codigo_venta += 1

    class Meta:
        ordering= ["codigo"]
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'





class Facturas(models.Model):
    ORIGINAL = 1
    DUPLICADO = 2
    TRIPLICADO = 3
    choices = [
        (ORIGINAL, 'Original'),
        (DUPLICADO, 'Duplicado'),
        (TRIPLICADO, 'Triplicado'),
    ]
    moneda = models.FloatField(verbose_name='Moneda')
    fecha_de_factura = models.DateTimeField(null=True, editable=True, verbose_name='Fecha de Facturación')
    codigo=models.IntegerField(verbose_name='Código',unique=True)
    venta = models.OneToOneField(Ventas,on_delete=models.PROTECT)
    empresa = models.OneToOneField(Empresa,on_delete=models.PROTECT)
    copia = models.CharField(max_length=1, choices=choices,verbose_name='Copia',default=ORIGINAL,unique=False,null=False)

    def __init__(self):
        global codigo_factura
        self.codigo = codigo_factura
        codigo_factura += 1

    class Meta:
        ordering= ["codigo"]
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
