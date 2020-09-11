from django.contrib.auth.decorators import login_required
from django.urls import path

from homepage.views import MyHomePage

urlpatterns= [
    path('', login_required(MyHomePage.as_view()), name="homepage"),
]