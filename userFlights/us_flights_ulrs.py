from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reserve/$', views.gotoreserve, name='reserve'),
    url(r'^reservequery/$', views.reservequery, name='reservequery'),
]
