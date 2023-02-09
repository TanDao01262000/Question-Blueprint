from django.shortcuts import render, redirect
from . forms import UserRegisterForm

# Create your views here.
def login(request):
    return redirect('login')

def logout(request):
    return redirect('logout')

def register(request):
    form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})