from django.shortcuts import render
from royalFlight.db import mydb

path = "adminFlights/templates/"

def index(request):
    # Query to Gather Info about The Whole Flights
    return render(request, template_name=path + "index.html")


def details(request):  # Takes The ID of The Flight as a Parameter
    # Query to Gather Info about The Specific Chosen Flight

    return render(request, template_name=path + "details")
