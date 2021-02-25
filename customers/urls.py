from django.urls import path

from customers.views import ShowCustomers, AddCustomer, DeleteCustomer

app_name = "customers"

urlpatterns = [
    path('', ShowCustomers.as_view(), name='customers-list'),
    path('add/', AddCustomer.as_view(), name='add-customer'),
    path('<int:id>/delete/', DeleteCustomer.as_view(), name='delete-customer'),
]