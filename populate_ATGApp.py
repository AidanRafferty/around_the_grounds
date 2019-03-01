import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around_the_grounds.settings')
import django 
django.setup()
from django.contrib.auth.models import User
from ATGApp.models import UserProfile, Stadium, Review

def generate_user():

    new_user = User.objects.create(username = "aidan6")
    new_user.first_name="Aidan"
    new_user.last_name="Rafferty"
    
    new_user.save()

    p = UserProfile.objects.get_or_create(user=new_user)
    p.save()
    print(p)

if __name__== '__main__':
    print("Created the new user profile ")
    generate_user()


