from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"general/home.html")

def Calculator(request):
    if request.method == "POST":
        current = request.POST['electricity']   # In units = KWH
        gas = request.POST['LPG']   # In grams
        vehicle = request.POST['vehicle']   # Car , Bus

        if (vehicle == "Car"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
        elif (vehicle == "Bus"):
            bus_fuel = request.POST['fuel']     # Data is shared in the group

        # Calculator algo here
        
    return render(request,'general/home.html')