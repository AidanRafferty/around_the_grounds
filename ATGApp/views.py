from django.shortcuts import render
from django.http import HttpResponse
from ATGApp.models import Review, Stadium
from ATGApp.forms import UserForm, UserProfileForm

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
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'atgapp/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def account(request):
    context_dict = {}
    return render(request,'ATGApp/myAccount.html', context = context_dict)
