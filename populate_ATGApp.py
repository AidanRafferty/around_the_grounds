import os

import django
from ATGApp.models import Review, Stadium, UserProfile
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'around_the_grounds.settings')
django.setup()

def generate_user():

    new_user = User.objects.create(username = "aidan3")
    new_user.first_name="Aidan"
    new_user.last_name="Raff"
    new_user.save()

    p = UserProfile.objects.create(user=new_user)
    print(p)
    p.save()

if __name__== '__main__':
    print("starting to create users... ")
    generate_user()
