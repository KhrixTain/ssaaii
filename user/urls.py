from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import MyLoginView

app_name="user"
urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', login_required(LogoutView.as_view()), name="logout")

]