from django.db import models

# Create your models here.

codigo_cliente=1
codigo_articulo=1
codigo_venta=1
codigo_factura = 1

class Clientes(models.Model):
    GENERAL = 'G'
    REDUCIDO = 'R'
    SUPERREDUCIDO = 'S'
    EXENTO = 'E'
    choices = [
        (GENERAL, 'General'),
        (REDUCIDO, 'Reducido'),
        (SUPERREDUCIDO, 'Superreducido'),
        (EXENTO, 'Exento')
    ]
    credito_maximo = models.FloatField(null=True, blank=True, default=0)
    estado_cliente = models.BooleanField(verbose_name='Estado de cliente')
    tipo_cliente = models.CharField(max_length=1, verbose_name='Tipo de cliente')
    categoria_iva = models.CharField(max_length=1, choices=choices, verbose_name='Categoria IVA', unique=True, null=False)
    telefono = models.TextField(verbose_name='Telefono')
    cuit = models.TextField(verbose_name='CUIT', unique=True)
    e_mail = models.TextField(verbose_name='e-mail')
    codigo_postal = models.IntegerField(verbose_name='Codigo postal')
    fecha_nac = models.DateTimeField(null=True, editable=True, verbose_name='Fecha del nacimiento')
    nombre = models.TextField(verbose_name='Nombre')
    piso = models.IntegerField(verbose_name="Piso")
    departamento = models.CharField(max_length=20, verbose_name="Departamento")
    calle = models.TextField(verbose_name='Calle')
    numero = models.IntegerField(verbose_name='Numero')
    codigo = models.IntegerField(verbose_name='Codigo de cliente', unique=True)
    fecha_cre = models.DateTimeField(null=True, editable=True, verbose_name='Fecha de Creacion')

    def __init__(self):
        global codigo_cliente
        self.codigo = codigo_cliente
        codigo_cliente += 1

    class Meta:
        ordering= ["cuit"]
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

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
