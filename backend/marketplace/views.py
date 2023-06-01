from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'marketplace/productcard.html')

def Card(request):
    return render(request,'marketplace/productcard.html')