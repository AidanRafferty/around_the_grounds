# This is the urls module for the ATGApp Application
from django.conf.urls import url
from ATGApp import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

]
