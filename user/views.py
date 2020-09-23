from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from misitio import settings as setting

# Create your views here.
from django.views.generic import RedirectView

class MyLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {
        'title': "Inicio de Sesión",
    }
    def dispatch(self, request, *args, **kwargs):
        #En caso de que el usuario ya se hubiera loggeado
        #Es redirigido al LOGIN_REDIRECT_URL
        #En caso de que no setuviera loggeado, le muestra
        #El login normal
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request,args,kwargs)



