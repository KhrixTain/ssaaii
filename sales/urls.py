from django.contrib.auth.decorators import login_required
from django.urls import path
from sales.views import *
from articles.views import *


app_name="sales"
urlpatterns = [
    path('', login_required(MySalesPage.as_view()),name="sales"),
    path('CargaVenta/', login_required(VentasView.as_view()), name="CargaVenta"),
    path('ABMarticles/',login_required(MySalesPage.as_view()), name="ABMarticles"),


]