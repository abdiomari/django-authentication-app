from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'],password2=form.cleaned_data['password2'], )
            return redirect('login.html')
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index.html')
            else:
                print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')