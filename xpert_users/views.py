from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User

# Create your views here.


def register_user(request):
    """creates a new user object"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect("login")
    else:
        form =  UserRegistrationForm()
    
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)


def login_user(request):
    """Logs in registered users into the application"""
    # user = request.user
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if user.account_type == "Service provider":
            #     return redirect('dashboard')
            # elif user.account_type == "Service seeker":
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {
        "form": form,
    }

    return render(request, "registration/login.html", context)


def logout_user(request):
    """logs out user from current session"""
    logout(request)
    return redirect('home')
    # context = {}
    # return render(request, "registration/logout.html", context)
    

def profile_detail(request, id):
    """displays user profiles for each user"""
    user = User.objects.get(pk=id)
    context = {'user': user}
    return render(request, 'xpert_users/profile_detail.html', context)