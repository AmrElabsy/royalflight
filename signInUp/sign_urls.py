from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signin-admin$', views.signinadmin, name='signin'),
    url(r'^login-admin$', views.loginadmin, name='signin'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^logout-user/$', views.logoutuser, name='logout'),
    url(r'^logout-admin/$', views.logoutadmin, name='logout'),
    ]
