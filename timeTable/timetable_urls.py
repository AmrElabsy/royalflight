from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<time_table_id>[0-9]+)/edit/$', views.gotoedit, name='edit'),
    url(r'^editquery/$', views.editquery, name='editquery'),
    url(r'^add/$', views.gotoadd, name='add'),
    url(r'^addquery$', views.addquery, name='addquery'),
]
