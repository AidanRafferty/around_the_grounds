import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around_the_grounds.settings')
import django 
django.setup()
from django.contrib.auth.models import User
from ATGApp.models import UserProfile, Stadium, Review

def generate_user():

    # Create the first new user
    new_user = User.objects.get_or_create(username = "ABC")[0]
    new_user.first_name="Joe"
    new_user.last_name="Bloggs"
    new_user.save()
    p = UserProfile.objects.create(user=new_user)
    p.save()

    # Create a second new user 
    new_user2 = User.objects.get_or_create(username = "DEF")[0]
    new_user2.first_name="John"
    new_user2.last_name="Smith"
    new_user2.save()
    p2 = UserProfile.objects.create(user=new_user2)
    p2.save()

    new_user3 = User.objects.get_or_create(username = "LiverpoolFan")[0]
    new_user3.first_name="Craig"
    new_user3.last_name="Gunn"
    new_user3.save()
    p3 = UserProfile.objects.create(user=new_user3)
    p3.save()




    # then a dictionary of stadiums for the users to add 
    Old_Trafford_Reviews = [
        {"atmosphere": 4,
        "food": 3, 
        "facilities": 4,
        "additionalInfo":"What a place",
        },
        {"atmosphere": 5,
        "food": 5, 
        "facilities": 5,
        "additionalInfo":"Brilliant day",
        }]
    
    Camp_Nou_Reviews = [
        {"atmosphere": 5,
        "food": 5, 
        "facilities": 5,
        "additionalInfo":"Incredible",
        },
        {"atmosphere": 5,
        "food": 5, 
        "facilities": 5,
        "additionalInfo":"Football's greatest",
        }]

    
    Stadiums = {"Old Trafford": {"Reviews": Old_Trafford_Reviews,
        "capacity":76000,
        "postcode":"M16ORA",
        "description": "The theatre of dreams",
        "hometeam": "Manchester United FC",
        "TotalScore": 26,
        "ReviewCount":2},
        "Camp Nou": {"Reviews": Camp_Nou_Reviews,
        "capacity": 99354,
        "postcode":"08028 Barcelona",
        "description": "The home of Barcelona Football Club",
        "hometeam": "FC Barcelona",
        "TotalScore":30,
        "ReviewCount":2}}





    for stadium, stadiumData in Stadiums.items():
        
        print(stadiumData["capacity"])

        s = add_stadium(stadium, stadiumData["capacity"], stadiumData["postcode"], stadiumData["description"], stadiumData["hometeam"], stadiumData["TotalScore"], stadiumData["ReviewCount"], p2)
        
        print(s)

        for review in stadiumData["Reviews"]:

            add_review(s, p, review["atmosphere"], review["food"], review["facilities"], review["additionalInfo"])


    add_stadium("Anfield", 54074, "L4 OTH", 
    "Anfield is the home of Liverpool Football club since 1892 and is the sixth largest football staium in England. The stadium was originally owned by Merseyside rivals Everton until a club dispute led to the Toffees moving to their current ground Goodison Park", 
    "Liverpool FC", 0, 0, p3)

    
    for s in Stadium.objects.all():

        for r in Review.objects.all():

            print("- {0} - {1} ".format(str(s), str(r)))

def add_stadium(name, capacity, postcode, description, hometeam, totalScore, reviewCount, user):

    print("This is inside the add stadium function\n",name, capacity, postcode, description, hometeam, totalScore, reviewCount, user)

    stadium = Stadium.objects.create(name=name, user=user)

    print(stadium.name)
    stadium.description = description
    stadium.capacity = capacity
    stadium.postcode = postcode
    stadium.homeTeam = hometeam
    stadium.TotalScore = totalScore
    stadium.ReviewCount = reviewCount

    stadium.save()

    print(stadium,"-",stadium.user,"-",stadium.slug)

    return stadium

def add_review(stadium, user, atmosphere, food, facilities, Info):

    review = Review.objects.create(stadium=stadium, user=user)
    review.atmosphere = atmosphere
    review.food = food
    review.facilities = facilities
    review.additionalInfo = Info

    review.save()

    print(review)
    
    return review


    # then need a dictionary of reviews made by users on the stadiums



    # need to remember to hard code the field entry for the reviews
    # counter and the totalScore in the stadium records as they can't be 
    # dynamically calculated yet. 


if __name__== '__main__':
    print("Created the new user profile ")
    generate_user()


