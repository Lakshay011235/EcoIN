from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'general\home.html')

def Login(request):
    return render(request,'general/login.html')