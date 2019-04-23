from django.shortcuts import render
from royalFlight.db import mydb

path = "userProfile/templates/"
stmt = mydb.cursor(buffered=True)

def index(request):
    return indexRec(request)


def gotoedit(request):
    id = request.session['clientid']
    stmt.execute("SELECT * FROM client WHERE clnt_ID = " + str(id))
    result = stmt.fetchone()
    context = {
        'client': result
    }
    return render(request, template_name=path + "edit.html", context=context)


def editquery(request):

    if request.POST:
        id = request.session['clientid']
        name = request.POST['name']
        mail = request.POST['email']
        password = request.POST['pass']
        phone = request.POST['phone']
        address = request.POST['address']
        ccN = request.POST['Credit']

        sql = "UPDATE client SET clnt_name = %s, clnt_email = %s, clnt_pass = %s, clnt_phone = %s, clnt_address = %s, clnt_ccnumber = %s WHERE clnt_ID = %s"
        val = (name, mail, password, phone, address, ccN, id)
        stmt.execute(sql, val)
        mydb.commit()

    return indexRec(request)


def tranactions(request):
    id = request.session['clientid']
    stmt.execute("SELECT transactions.*, flights.flt_date, timetable.tt_start, timetable.tt_end FROM transactions INNER JOIN flights ON transactions.tr_flight = flights.flt_ID INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE tr_client = " + str(id) + " AND DATE(flt_date) < CURDATE()")
    result = stmt.fetchall()
    context = {
        'transactions': result,
    }
    return render(request, template_name=path + "myTransactions.html", context=context)

def reservations(request):
    id = request.session['clientid']
    stmt.execute("SELECT transactions.*, flights.flt_date, timetable.tt_start, timetable.tt_end FROM transactions INNER JOIN flights ON transactions.tr_flight = flights.flt_ID INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE tr_client = " + str(id) + " AND DATE(flt_date) > CURDATE()")
    result = stmt.fetchall()
    context = {
        'reservations': result,
    }
    return render(request, template_name=path + "reservations.html", context=context)


def gotoeditreservation(request, flight_id):
    """stmt = mydb.cursor()
    stmt.execute(
        "SELECT flights.*, timetable.*, transactions.tr_ID FROM flights INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID  INNER JOIN transactions ON flights.flt_ID = transactions.tr_flight WHERE flt_ID = " + str(flight_id))
    result = stmt.fetchone()

    context = {
        'flight': result,
    }"""
    return render(request, template_name=path + "editReservation.html", context=context)


def editreservationquery(request):

    """if request.POST:
        trans_id = request.POST["trans_id"]
        priceA = request.POST['priceA']
        priceB = request.POST['priceB']
        priceC = request.POST['priceC']

        if request.POST['flightClass'] == "ClassA":
            price = priceA
        elif request.POST['flightClass'] == "ClassB":
            price = priceB
        else:
            price = priceC

        sql = "UPDATE transactions SET tr_price = " + price +  " WHERE tr_ID = " + trans_id
        val = (price, trans_id)

        stmt.execute("UPDATE transactions SET tr_price = " + price +  " WHERE tr_ID = " + trans_id)
        mydb.commit()

    stmt.execute(
        "SELECT flights.*, timetable.tt_end, timetable.tt_hour_start, timetable.tt_hour_end FROM flights INNER JOIN timetable ON flights.flt_timetable = timetable.tt_ID WHERE DATE(flt_date) > CURDATE() ORDER BY flt_id ASC LIMIT 50")
    result = stmt.fetchall()
    context = {
        'flights': result,
    }"""

    return indexRec(request)


def indexRec(request):
    id = request.session['clientid']
    stmt.execute("SELECT * FROM client WHERE clnt_ID = " + str(id))
    result = stmt.fetchone()
    context = {
        'client': result
    }
    return render(request, template_name=path + "index.html", context=context)
