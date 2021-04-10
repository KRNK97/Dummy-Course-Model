from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html', locals())


class LoginUserView(LoginView):
    success_url = 'home'
    template_name = 'users/login.html'
