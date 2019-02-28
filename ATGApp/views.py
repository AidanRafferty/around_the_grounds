from django.shortcuts import render
from django.http import HttpResponse
from ATGApp.models import Review
# Create your views here.


def index(request):
    #Returns information on highest rated stadium
    #Returns picture of highest rated stadium
    
    highestRatedStadium = Review.objects.order_by('-totalScore')[:1]
    context_dict = {'highestRatedStadium' : highestRatedStadium}
    response = render(request,'atg/index.html',context = context_dict)
    return response

def stadiums(request):
    return render(request, 'atg/stadiums.html', context = context_dict)

def login(request):
    return render(request, 'atg/login.html', context=context_dict)

def register(request):
    return render(request, 'atg/register.html', context=context_dict)




