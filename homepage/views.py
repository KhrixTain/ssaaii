from django.views.generic import TemplateView

class MyHomePage(TemplateView):
    template_name = 'homepage.html'
    extra_context = {
        'title': "Página Principal",
    }
class LibroDiarioView(TemplateView):
    template_name = 'libro_diario_view.html'
    extra_context = {
        'title': "Libro Diario",
    }