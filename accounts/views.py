from atexit import register
import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.
def registerView(request):
    form= CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Account was created successfully')
            return redirect('blinder:profile')
    else:
        form=CreateUserForm()
    return render(request, 'registeration/signup.html', {'form':form})