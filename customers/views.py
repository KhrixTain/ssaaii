from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DeleteView

from customers.forms import CustomerForm
from customers.models import Clientes, Customer


class ShowCustomers(ListView):
    model = Customer
    template_name = "clientes_list.html"
    paginate_by = 20
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddCustomer(CreateView):
    model = Customer
    #fields = ['name']
    template_name = 'cliente_add.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customers-list')

class DeleteCustomer(DeleteView):
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('customers:customers-list')
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id_)


