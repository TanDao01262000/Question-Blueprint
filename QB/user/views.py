from django.shortcuts import render, redirect
from . forms import UserRegisterForm, ProfileUpdateForm, UserInfoUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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


@login_required
def profile_view(request):
    return render(request, 'user/profile.html', {})


@login_required
def update_profile(request):
    cur_user_obj = {
        'username' : request.user.username,
        'email': request.user.email,
    }
    cur_user_profile = {
        'username' : request.user.profile.bio,
        'image': request.user.profile.image.url,
    }
    if request.method == "POST":
        user_update_form = UserInfoUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Update successfully')
            return redirect('profile_view')
    else:
        user_update_form = UserInfoUpdateForm(initial=cur_user_obj)
        profile_update_form = ProfileUpdateForm(initial=cur_user_profile)
    context = {
        'user_update_form' : user_update_form,
        'profile_update_form' : profile_update_form,
    }

    return render(request, 'user/update.html', context=context)