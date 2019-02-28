from django.shortcuts import render
from django.http import HttpResponse
from ATGApp.forms import Review
# Create your views here.


def index(request):
    #Needs highest rated stadium
    #Order TotalScore and choose top
    #Return in context dictionary

    return HttpResponse("The ATG App Index view")




