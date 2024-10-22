from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', {'form': form})
        form.cleaned_data.pop('password_confirm')
        user = User.objects.create(**form.cleaned_data)
        login(request, user)
        return redirect('/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'login.html', {'form': form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error(None, "Username or password is incorrect")
            return render(request, 'login.html', {'form': form})
        else:
            login(request, user)
        return redirect('/')
