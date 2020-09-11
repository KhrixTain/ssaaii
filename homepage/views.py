from django.views.generic import TemplateView

class MyHomePage(TemplateView):
    template_name = 'homepage.html'
    extra_context = {
        'title': "Página Principal",
    }
