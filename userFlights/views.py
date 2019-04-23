from django.shortcuts import render
from royalFlight.db import mydb

path = "userFlights/templates/"

def index(request):
    stmt = mydb.cursor()

    stmt.execute("SELECT flights.*, timetable.tt_end, timetable.tt_hour_start, timetable.tt_hour_end FROM flights INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE DATE(flt_date) > CURDATE() ORDER BY flt_id ASC LIMIT 50")
    result = stmt.fetchall()
    context = {
        'flights': result,
    }

    return render(request, template_name=path + "index.html", context=context)


def gotoreserve(request, flight_id):
    stmt = mydb.cursor()
    stmt.execute("SELECT flights.*, timetable.*  FROM flights INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE flt_ID = " + str(flight_id))
    result = stmt.fetchone()

    context = {
        'flight': result,
    }
    return render(request, template_name=path + "reserve.html", context=context)


def reservequery(request):
    stmt = mydb.cursor()
    if request.POST:
        id = request.session['clientid']
        flight_id = request.POST["flight_id"]
        priceA = request.POST['priceA']
        priceB = request.POST['priceB']
        priceC = request.POST['priceC']

        if request.POST['flightClass'] == "ClassA":
            price = priceA
        elif request.POST['flightClass'] == "ClassB":
            price = priceB
        else:
            price = priceC
        sql = "INSERT INTO transactions(tr_client, tr_flight, tr_price, tr_time) VALUES (%s, %s, %s, now())"
        val = (id, flight_id, price)

        stmt.execute(sql, val)
        mydb.commit()

    stmt.execute("SELECT flights.*, timetable.tt_end, timetable.tt_hour_start, timetable.tt_hour_end FROM flights INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE DATE(flt_date) > CURDATE() ORDER BY flt_id ASC LIMIT 50")
    result = stmt.fetchall()
    context = {
        'flights': result,
    }


    return render(request, template_name=path + "index.html", context=context)

