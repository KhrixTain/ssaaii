from django.contrib.auth.decorators import login_required
from django.urls import path

from account.views import MyLoginView, MyHomePage

urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),
    path('', login_required(MyHomePage.as_view()), name="homepage"),
    path('', MyHomePage.as_view(), name="homepage" ),
]