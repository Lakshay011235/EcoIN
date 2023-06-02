from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request,'carbonfootprint/perspective.html')

def IndividualCalculator(request):
    if request.method == "POST":
        emission = 0
        current = float(request.POST['electricity'])   # In units = KWH
        gas = float(request.POST['gas'])   # In grams
        vehicle = request.POST['vehicle']   # Car , Bus
        milage = float(request.POST['mileage'])
        distance =float( request.POST['distance'])
        emissions_factor = 0

        if (vehicle == "Car"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
            if car_fuel == 'gasoline':
                emissions_factor = 2.31  # in kg CO2 per liter
            elif car_fuel == 'diesel':
                emissions_factor = 2.68  # in kg CO2 per liter
        elif (vehicle == "Bus"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
            emissions_factor = 0.68  # in kg CO2 per km

        # Fuel

        if vehicle == 'car':
            emission = (distance / milage) * emissions_factor
        elif vehicle == 'bus':
            emission = distance * emissions_factor
        # Electricity
        emissions_factor = 0.93
        emission = emission + current*emissions_factor
        
        #LPG
        emissions_factor = 2.983
        emission = emission + emissions_factor*gas
        return render(request,"carbonfootprint/individual.html", context={"emission" : emission})
    return render(request,"carbonfootprint/individual.html")

def BusinessCalculator(request):
    return render(request,"general/home.html")