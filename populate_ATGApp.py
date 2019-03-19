import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around_the_grounds.settings')
import django 
django.setup()
from django.contrib.auth.models import User
from ATGApp.models import UserProfile, Stadium, Review

from django.core.files import File

def generate_user():

    print("This is the file path for images below")
    print()


    image_path = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'around_the_grounds', 'static', 'images'))

   
    print()
    print(str(image_path))
    print()
    old_trafford_image = open(os.path.join(image_path, 'OldTrafford.jpg'), 'rb')
    celtic_park_image = open(os.path.join(image_path, 'celtic-park.jpg'), 'rb')
    anfield_image = open(os.path.join(image_path, 'Anfield.jpg'), 'rb')
    allianz_image = open(os.path.join(image_path, 'Allianz.jpg'), 'rb')
    nou_image = open(os.path.join(image_path, 'NouCamp.jpg'), 'rb')    
    

    OTFile = File(old_trafford_image, 'rb')
    CelticFile = File(celtic_park_image, 'rb')
    CampFile = File(nou_image, 'rb')
    AllianzFile = File(allianz_image, 'rb')
    AnfieldFile = File(anfield_image, 'rb')

    # Create sample users for the website and thier associated profiles
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

    new_user4 = User.objects.get_or_create(username = "TartanArmy101")[0]
    new_user4.first_name="Davie"
    new_user4.last_name="Shakespeare"
    new_user4.save()
    p4 = UserProfile.objects.create(user=new_user4)
    p4.save()


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

    
    Stadiums = {"Old Trafford": 
    {"Reviews": Old_Trafford_Reviews,
    "capacity":76000,
    "postcode":"M16ORA",
    "description": "The theatre of dreams",
    "hometeam": "Manchester United FC",
    "TotalScore": 26,
    "ReviewCount":2,
    "photo":OTFile},

        "Camp Nou": {"Reviews": Camp_Nou_Reviews,
        "capacity": 99354,
        "postcode":"08028 Barcelona",
        "description": "The home of Barcelona Football Club",
        "hometeam": "FC Barcelona",
        "TotalScore":30,
        "ReviewCount":2,
        "photo":CampFile}}

    add_stadium("Anfield", 54074, "L4 OTH", 
    "Anfield is the home of Liverpool Football club since 1892 and is the sixth largest football staium in England. The stadium was originally owned by Merseyside rivals Everton until a club dispute led to the Toffees moving to their current ground Goodison Park", 
    "Liverpool FC", 0, 0, p3, AnfieldFile)

    add_stadium("Allianz Arena", 75000, 
    "80939 München, Germany", 
    "The Allianz Arena replaced Munich’s old Olympiastadion. First plans for a new stadium were made in 1997, and even though the city of Munich initially preferred reconstructing the Olympiastadion, they eventually went ahead with the clubs’ proposal for an entire new stadium.", 
    "FC Bayern Munich", 0,0,p2, AllianzFile)

    add_stadium("Celtic Park", 60832, "G403RE", 
    "Celtic Park, also known as paradise and Parkhead, is home to Celtic Football Club, the champions of the Scottish Permiership and the double treble winners.", 
    "Celtic FC", 0, 0, p4, CelticFile)

    for stadium, stadiumData in Stadiums.items():
    
        s = add_stadium(stadium, stadiumData["capacity"], stadiumData["postcode"], stadiumData["description"], stadiumData["hometeam"], stadiumData["TotalScore"], stadiumData["ReviewCount"], p2, stadiumData["photo"])
        
        print(s)

        for review in stadiumData["Reviews"]:

            add_review(s, p, review["atmosphere"], review["food"], review["facilities"], review["additionalInfo"])

    for s in Stadium.objects.all():

        for r in Review.objects.all():

            print("- {0} - {1} ".format(str(s), str(r)))

    old_trafford = Stadium.objects.get(name="Old Trafford")

    add_review(old_trafford, p4, 3,3,3,"Glory Glory Man United")
    
    allianz_arena = Stadium.objects.get(name="Allianz Arena")
    
    add_review(allianz_arena, p2, 5,5,5,"Best atmosphere in Germany.")

def add_stadium(name, capacity, postcode, description, hometeam, totalScore, reviewCount, user, photo):
    print("This is inside the add stadium function\n",name, capacity, postcode, description, hometeam, totalScore, reviewCount, user)

    stadium = Stadium.objects.create(name=name, user=user)

    print(stadium.name)
    stadium.description = description
    stadium.capacity = capacity
    stadium.postcode = postcode
    stadium.homeTeam = hometeam
    stadium.TotalScore = totalScore
    stadium.ReviewCount = reviewCount
    stadium.photo = photo

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


