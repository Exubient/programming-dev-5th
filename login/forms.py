from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username = user.email
        user.firstname = self.cleaned_data["first_name"]
        user.lastname = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    check = forms.IntegerField()
    class Meta:
        model=User
        fields='__all__'



