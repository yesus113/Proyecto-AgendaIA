from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, RedirectView
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from agenda import settings

# Create your views here.
def hello(request):
    return HttpResponse("Hola mundo")

class LoginFormView(LoginView):
    template_name = 'login/login.html'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    
class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)