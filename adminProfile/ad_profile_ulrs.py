from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', views.gotoedit, name='edit'),
    url(r'^editquery/$', views.editquery, name='editquery'),

]
