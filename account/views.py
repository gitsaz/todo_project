from django.shortcuts import render, redirect
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
from .form import UserRegistrationForm , UserLoginForm

# Create your views here.
def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Wrong Credential")
                
    return render(request, 'login.html', {"form": form})



def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')