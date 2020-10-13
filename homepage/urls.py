from django.contrib.auth.decorators import login_required
from django.urls import path


from homepage.views import MyHomePage, LibroMayor

urlpatterns = [
    path('', login_required(MyHomePage.as_view()), name="homepage"),
    path('libroMayor/', login_required(LibroMayor.as_view()), name="libroMayor"),
]