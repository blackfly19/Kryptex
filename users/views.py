from django.shortcuts import render

def signUpPage(request):
    return render(request, 'users/signUp.html')
