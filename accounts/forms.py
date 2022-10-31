from dataclasses import field
from importlib import import_module
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1', 'password2',]