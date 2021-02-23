from django.contrib import admin
from django.urls import path, include

from homepage.views import Main

urlpatterns = [
    path('', Main.as_view(), name="main"),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls',namespace="user")),
    path('homepage/', include('homepage.urls',namespace="homepage")),
    path('sales/', include('sales.urls',namespace="sales")),
    path('articles/', include('articles.urls',namespace="articles")),

]