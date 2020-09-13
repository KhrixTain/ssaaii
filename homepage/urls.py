from django.contrib.auth.decorators import login_required
from django.urls import path

from account.view.librodiario.view import LibroDiarioView
from homepage.views import MyHomePage

urlpatterns = [
    path('', login_required(MyHomePage.as_view()), name="homepage"),
    path('libro_diario_view/', LibroDiarioView.as_view(), name="librodiarioview"),
]