from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request,'carbonfootprint/perspective.html')

def IndividualCalculator(request):
    if request.method == "POST":
        emission = 0
        current = request.POST['electricity']   # In units = KWH
        gas = request.POST['gas']   # In grams
        vehicle = request.POST['vehicle']   # Car , Bus
        milage = request.POST['mileage']
        distance = request.POST['distance']

        if (vehicle == "Car"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
        elif (vehicle == "Bus"):
            bus_fuel = request.POST['fuel']     # Data is shared in the group

        # Fuel

        # Electricity
        
        return HttpResponse("<h1> You carbon emission is:"+str(emission)+" </h1>")
    return render(request,"carbonfootprint/individual.html")

def BusinessCalculator(request):
    return render(request,"general/home.html")