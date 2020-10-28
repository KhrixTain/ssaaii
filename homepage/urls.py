from django.contrib.auth.decorators import login_required
from django.urls import path


from homepage.views import MyHomePage, LibroMayor, CargarAsiento
app_name="homepage"
urlpatterns = [
    path('', login_required(MyHomePage.as_view()),name="homepage"),
    path('cargar-asiento/', login_required(CargarAsiento.as_view()), name="cargar-asiento"),
    path('libroMayor/', login_required(LibroMayor.as_view()), name="libroMayor"),
]