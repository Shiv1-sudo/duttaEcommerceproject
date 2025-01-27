'''from django.shortcuts import render

# Create your views here.'''
from django.shortcuts import render
from django.views import View

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')

class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

