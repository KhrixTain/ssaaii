# Generated by Django 3.1.3 on 2021-01-28 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_item', models.IntegerField(unique=True, verbose_name='Código Item')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('existencia', models.FloatField(verbose_name='Existencia')),
                ('item_suspendido', models.BooleanField(verbose_name='Item suspendido')),
                ('motivo_suspension', models.TextField(verbose_name='Motivo suspension')),
                ('deposito', models.IntegerField(verbose_name='Deposito')),
                ('codigo_barra', models.IntegerField(verbose_name='Código de barras')),
                ('observacion', models.TextField(verbose_name='Observaciones')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('stock_comprometido', models.FloatField(verbose_name='Stock Comprometido')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credito_maximo', models.FloatField(blank=True, default=0, null=True)),
                ('estado_cliente', models.BooleanField(verbose_name='Estado de cliente')),
                ('tipo_cliente', models.CharField(max_length=1, verbose_name='Tipo de cliente')),
                ('categoria_iva', models.CharField(choices=[('G', 'General'), ('R', 'Reducido'), ('S', 'Superreducido'), ('E', 'Exento')], max_length=1, unique=True, verbose_name='Categoria IVA')),
                ('telefono', models.TextField(verbose_name='Telefono')),
                ('cuit', models.TextField(unique=True, verbose_name='CUIT')),
                ('e_mail', models.TextField(verbose_name='e-mail')),
                ('codigo_postal', models.IntegerField(verbose_name='Codigo postal')),
                ('fecha_nac', models.DateTimeField(null=True, verbose_name='Fecha del nacimiento')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('piso', models.IntegerField(verbose_name='Piso')),
                ('departamento', models.CharField(max_length=20, verbose_name='Departamento')),
                ('calle', models.TextField(verbose_name='Calle')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo de cliente')),
                ('fecha_cre', models.DateTimeField(null=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['cuit'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('cuit', models.TextField(unique=True, verbose_name='CUIT')),
                ('razon_social', models.TextField(verbose_name='Razón Social')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('telefono', models.TextField(verbose_name='Telefono')),
                ('e_mail', models.TextField(verbose_name='e-mail')),
                ('fecha_inicio_actividades', models.DateTimeField(null=True, verbose_name='Fecha de inicio de Actividades')),
                ('ingresos_brutos', models.TextField(default=models.TextField(unique=True, verbose_name='CUIT'))),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('dni', models.TextField(unique=True, verbose_name='DNI')),
                ('codigo', models.TextField(verbose_name='Vendedor')),
                ('fecha_de_ingreso', models.DateTimeField(null=True, verbose_name='Fecha de Ingreso')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportista', models.TextField(verbose_name='Transportista')),
                ('cobrador', models.TextField(verbose_name='Cobrador')),
                ('tipo_bonificacion', models.FloatField(verbose_name='Tipo de bonificación')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('porcentaje_descuento', models.FloatField(verbose_name='Porcentaje de Descuento')),
                ('descuento', models.FloatField(verbose_name='Descuento')),
                ('condicion_de_venta', models.CharField(choices=[('C', 'Contado'), ('T', 'Tarjeta_credito'), ('F', 'Financiacion'), ('H', 'Cheque')], max_length=1, verbose_name='Condición de Venta')),
                ('zona_fiscal', models.IntegerField(verbose_name='Zona fiscal')),
                ('entrega', models.TextField(verbose_name='Entrega')),
                ('articulo', models.ManyToManyField(to='sales.Articulos')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.clientes')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Rubros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True, verbose_name='Nombre')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('subrubro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.rubros')),
            ],
            options={
                'verbose_name': 'Rubro',
                'verbose_name_plural': 'Rubros',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneda', models.FloatField(verbose_name='Moneda')),
                ('fecha_de_factura', models.DateTimeField(null=True, verbose_name='Fecha de Facturación')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('copia', models.CharField(choices=[(1, 'Original'), (2, 'Duplicado'), (3, 'Triplicado')], default=1, max_length=1, verbose_name='Copia')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sales.empresa')),
                ('venta', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sales.ventas')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['codigo'],
            },
        ),
        migrations.AddField(
            model_name='articulos',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.rubros'),
        ),
    ]
