# Generated by Django 3.1.3 on 2021-02-26 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer'),
        ('sales', '0004_auto_20210224_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.clientes'),
        ),
    ]
