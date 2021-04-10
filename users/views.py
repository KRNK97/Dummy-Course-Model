from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import login
from django.contrib.auth.models import User


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html', locals())

    def post(self, request):
        try:
            user = User(first_name=request.POST.get('first_name'), last_name=request.POST.get(
                'last_name'), email=request.POST.get('email'), username=request.POST.get('email'))
            user.set_password(request.POST.get('password'))
            user.save()
        except Exception as e:
            print(e)
            return render(request, 'users/register.html', locals())

        return HttpResponseRedirect('/users/login')


class HomeView(View):
    def get(self, request):
        return HttpResponse(f"Home Page | Logged in as - {request.user}")
