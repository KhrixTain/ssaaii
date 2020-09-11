from django.contrib.auth.decorators import login_required
from django.urls import path

from account.views import MyLoginView

urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),
]