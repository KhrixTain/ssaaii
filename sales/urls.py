from django.contrib.auth.decorators import login_required
from django.urls import path
from sales.views import *
from articles.views import *


app_name="sales"
urlpatterns = [
    path('CargarVenta/', login_required(VentasView.as_view()), name="CargarVenta"),
]