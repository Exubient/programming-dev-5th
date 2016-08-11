from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound





# Create your views here.

def logout(request):
    logout(request)
    return render(request, 'login/login.html', {'form':forms})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'login/sign_up.html', {'form': form,
        })


def my_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        check = request.POST['check']
        user = authenticate(username=username, password=password)
        if check is not "6":
            return HttpResponseNotFound('<h1>you are bad in math</h1>')
        elif user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/accounts/profile')
            else:
                return HttpResponseNotFound('<h1>not available</h1>')
        else:
           return HttpResponseNotFound('<h1>password incorrect</h1>')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form':form})

