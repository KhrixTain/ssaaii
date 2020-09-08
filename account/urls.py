from django.urls import path

from account.views import MyLoginView, MyHomePage

urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),
    path('', MyHomePage.as_view(), name="homepage" ),
]