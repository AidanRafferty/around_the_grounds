from django.shortcuts import render
from django.http import HttpResponse
from ATGApp.models import Review, Stadium

def index(request):
    #Returns information on highest rated stadium
    #Returns picture of highest rated stadium

    highestRatedStadium = Stadium.objects.order_by('-totalScore')[:1]
    
    
    context_dict = {'highestRatedStadium' : highestRatedStadium}
    response = render(request,'ATGApp/index.html',context = context_dict)
    return response

def stadiums(request):
    context_dict = {}
    return render(request, 'ATGApp/stadiums.html', context = context_dict)

def login(request):
    context_dict = {}
    return render(request, 'ATGApp/login.html', context = context_dict)

def register(request):
    context_dict = {}
    return render(request, 'ATGApp/register.html', context = context_dict)

def account(request):
    context_dict = {}
    return render(request,'ATGApp/myAccount.html', context = context_dict)
