from django.contrib import admin
from articles.models import *
from sales.models import Ventas

admin.site.register(Articulos)
admin.site.register(Rubros)
admin.site.register(Ventas)
# Register your models here.
