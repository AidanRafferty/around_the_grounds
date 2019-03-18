from django.test import TestCase
from ATGApp.models import Stadium,UserProfile,User
from django.core.urlresolvers import reverse
import populate_ATGApp

def create_user():
    # Create a user
    user = User.objects.get_or_create(username="testuser", password="test1234",
                                      first_name="Test", last_name="User", email="testuser@testuser.com")[0]
    user.set_password(user.password)
    user.save()

    # Create a user profile
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_profile.save()

    return user, user_profile

class StadiumTests(TestCase):

    def test_stadium_name_slug(self):
        stadium = Stadium()
        stadium.name = 'Best Stadium In The World'
        stadium.user_id = 1
        stadium.save()
        self.assertEqual(stadium.slug,"best-stadium-in-the-world")

    def test_stadium_view(self):
        populate_ATGApp.populate()
        response = self.client.get(reverse('stadiums'))
        self.assertContains(response, "Best Stadium In The World")
        
        

        
        
        
