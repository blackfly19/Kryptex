from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from crypto.views import home


def signUpPage(request):
	if request.method == "POST":
		return redirect("main:crypto-home")
	return render (request=request, template_name="users/signUp.html")


def login(request):
	if request.method == "POST":
		return redirect('main:crypto-home')
	return render(request, 'users/signIn.html')
