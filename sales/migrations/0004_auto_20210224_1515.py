# Generated by Django 3.1.3 on 2021-02-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_ventas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='cliente',
            field=models.CharField(max_length=50, verbose_name='Cliente'),
        ),
    ]
