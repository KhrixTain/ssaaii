from django.contrib.auth.decorators import login_required
from django.urls import path
from articles.views import *


app_name="articles"
urlpatterns = [
    path('ABMarticles/',login_required(MySalesPage.as_view()), name="ABMarticles"),


]