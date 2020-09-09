<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> 35085625a5117446d383cdfe2867ad84cd5fb6ea
from django.urls import path

from account.views import MyLoginView, MyHomePage

urlpatterns=[
    path('login/', MyLoginView.as_view(), name="login"),
<<<<<<< HEAD
    path('', login_required(MyHomePage.as_view()), name="homepage"),
=======
    path('', MyHomePage.as_view(), name="homepage" ),
>>>>>>> 35085625a5117446d383cdfe2867ad84cd5fb6ea
]