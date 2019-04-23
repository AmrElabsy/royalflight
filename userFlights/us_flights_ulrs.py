from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reserve/(?P<flight_id>[0-9]+)/$', views.gotoreserve, name='reserve'),
    url(r'^reservequery$', views.reservequery, name='reservequery'),
]
