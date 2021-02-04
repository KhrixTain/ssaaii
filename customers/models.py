from django.db import models
codigo_cliente=1


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