from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def login(request):
    return redirect('login')

def logout(request):
    logout(request)
    return redirect('logout')

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created sucessfully for {username}. Login now")
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', {'form':form})