# This is the urls module for the ATGApp Application
from django.conf.urls import url
from ATGApp import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^stadiums/$', views.stadiums, name='stadiums'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/$', views.account, name='account'),

]
