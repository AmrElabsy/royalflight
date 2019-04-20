from django.shortcuts import render
from royalFlight.db import mydb

path = "main/templates/"


def index(request):
    request.session['username'] = "Amr"

    context = {

    }
    # del request.session['username']
    return render(request, template_name=path + "index.html", context=context)

