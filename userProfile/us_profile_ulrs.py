from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', views.gotoedit, name='edit'),
    url(r'^editquery/$', views.editquery, name='editquery'),
    url(r'^transactions/$', views.tranactions, name='transactions'),
    url(r'^editreservation$', views.gotoeditreservation, name='editreservation'),
    url(r'^editreservationquery$', views.editreservationquery, name='editreservationquery'),
]
