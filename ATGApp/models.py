from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import Sum

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

    def save(self,*args, **kwargs):

        self.slug = slugify(self.name)
        super(Stadium, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stadiums'

    def __str__(self):
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
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)



















