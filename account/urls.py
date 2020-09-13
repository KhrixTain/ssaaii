from django.contrib.auth.decorators import login_required
from django.urls import path, include

from account.views import MyLoginView


urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),

]