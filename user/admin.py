from django.contrib import admin
from homepage.models import *
from .models import *

admin.site.register(Cuentas)
admin.site.register(Cuenta_asientos)
admin.site.register(Asientos)
admin.site.register(Tipo_cuenta)
