from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('main.main_urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^planes/', include('planes.planes_ulrs')),
    url(r'^admin-flights/', include('adminFlights.ad_flights_url')),
    url(r'^admin-profile/', include('adminProfile.ad_profile_ulrs')),
    url(r'^budget/', include('budget.budget_urls')),
    url(r'^main/', include('main.main_urls')),
    url(r'^sign/', include('signInUp.sign_urls')),
    url(r'^timetable/', include('timeTable.timetable_urls')),
    url(r'^transactions/', include('transactions.transactions_urls')),
    url(r'^user-flights/', include('userFlights.us_flights_ulrs')),
    url(r'^user-profile/', include('userProfile.us_profile_ulrs')),


]
