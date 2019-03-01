from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.template.defaultfilters import slugify

# In order to get the highest rated stadium, use an sql query count total score
# then group by stadium which will show the stadium object and the total score across all reviews
# then order by count(totalScore) DESC

# This would be the SQL Query for sorting the stadium objects
# in descending order in terms of totalScore


# SELECT stadium, SUM(totalScore) FROM Reviews
# GROUP BY stadium
# ORDER BY totalScore DESC


# Create your models here.
# Create a Stadium table which will hold the data about each of the stadiums
# added that can be reviewed
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Stadium(models.Model):
    user = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    photo = models.ImageField(upload_to='stadium_images')
    capacity = models.IntegerField()
    postcode = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    homeTeam = models.CharField(max_length=55)
    slug = models.SlugField(unique=True)
    TotalScore = models.IntegerField(default=0)
    ReviewCount = models.IntegerField(default=0)

    def save(self,totalScore,*args, **kwargs):

        self.slug = slugify(self.name)
        self.ReviewCount += 1
        self.TotalScore += totalScore
        
        super(Stadium, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stadiums'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name 

class Review(models.Model):
    id = models.AutoField(primary_key=True) 
    atmosphere = models.IntegerField()
    food = models.IntegerField()
    facilities = models.IntegerField()
    additionalInfo = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now=True)
    totalScore = models.IntegerField(blank = True)
    user = models.ForeignKey(UserProfile)
    stadium = models.ForeignKey(Stadium)

    def save(self, *args, **kwargs):
        self.totalScore = self.atmosphere + self.food + self.facilities
<<<<<<< HEAD
        #Calls the save() function of the current stadium to increment the
        #ReviewTotal by 1 and to add the TotalScore of this review to the TotalScore for the stadium
        Stadium.save(self.stadium,self.totalScore)
=======
>>>>>>> 70b2ab47c28cfdb1520a1a13490f056235b2c51d
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
<<<<<<< HEAD
    
    def __repr__(self):
        return str(self.id) 



















=======
>>>>>>> 70b2ab47c28cfdb1520a1a13490f056235b2c51d
