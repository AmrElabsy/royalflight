from django.shortcuts import render
from royalFlight.db import mydb

path = "budget/templates/"

def index(request):
    stmt = mydb.cursor()
    stmt.execute("SELECT SUM(flt_cost) FROM flights")
    cost = stmt.fetchone()
    context = {
        'cost': cost[0]
    }

    stmt.execute("SELECT COUNT(flt_id) FROM flights")
    flights = stmt.fetchone()
    context['flights'] = flights[0]

    stmt.execute("SELECT COUNT(pln_id) FROM planes")
    planes = stmt.fetchone()
    context['planes'] = planes[0]

    stmt.execute("SELECT COUNT(clnt_id) FROM client")
    clients = stmt.fetchone()
    context['clients'] = clients[0]

    return render(request, template_name=path + "index.html", context=context)

