from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import *

# assigning User as our User model i.e. as User_details
User = get_user_model()

def Home(request):
    return render(request,'general\home.html')

def Login(request):
    if request.method == 'POST':
        print("Request recieved")
        username = request.POST['username']
        password = request.POST['password']

        print(f"username:{username}")

        if (request.POST['type'] == 'login'):
            new_user = authenticate(username=username,password=password)
            if new_user is not None:
                login(request,new_user)
                print("User logged in successfully")
            return redirect("Base:Home")
                
        if (request.POST['form-type'] == 'signup'):
            #Basic User details.
            email = request.POST['email']
            new_user = User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            login(request,new_user)
            return redirect('Base:Home')


    return render(request,'general\login.html')

def Logout(request):
    logout(request)
    return render(request,"general\home.html")