from django.shortcuts import render
from django.http import HttpResponse
from ATGApp.models import Review
# Create your views here.


def index(request):
    #Returns information on highest rated stadium
    #Returns picture of highest rated stadium

    highestRatedStadium = Review.objects.order_by('-totalScore')[:1]
    context_dict = {'highestRatedStadium' : highestRatedStadium}
    response = render(request,'ATGApp/index.html',context = context_dict)
    return response

def stadiums(request):
    return render(request, 'ATGApp/stadiums.html', context = context_dict)

def login(request):
    return render(request, 'ATGApp/login.html', context=context_dict)

def register(request):
    return render(request, 'ATGApp/register.html', context=context_dict)

def account(request):

    return render(request,'ATGApp/myAccount.html', context=context_dict)



