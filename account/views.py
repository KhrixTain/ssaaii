from django.contrib.auth.views import LoginView

# Create your views here.
from django.views.generic import FormView, TemplateView


class MyLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {
        'title': "Inicio de Sesión",
    }

class MyHomePage(TemplateView):
    template_name = 'homepage.html'