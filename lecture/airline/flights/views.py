from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flights,Passenger
# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flights.objects.all()
    })

def flight(request,flight_id):
    flight=Flights.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })

def book(request,flight_id):
    if request.method=="POST":
        flight = Flights.objects.get(pk=flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))