from django.contrib.auth.models import User
from django import  forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: #information about your class
        model = User
        fields = ['username', 'email', 'password'] # which field we want to show up

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: #information about your class
        model = User
        fields = ['username', 'password'] # which field we want to show up
