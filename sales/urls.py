from django.contrib.auth.decorators import login_required
from django.urls import path
from sales.views import *

app_name="sales"
urlpatterns = [
    path('CargaVenta/', login_required(VentasView.as_view()), name="CargaVenta"),
]