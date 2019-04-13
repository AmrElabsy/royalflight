from django.shortcuts import render
from royalFlight.db import mydb

path = "transactions/templates/"

def index(request):
    return render(request, template_name=path + "index.html")

