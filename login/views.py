from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render




# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'login/sign_up.html', {'form': form,
        })
