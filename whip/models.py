from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Criteria(models.Model):
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1024)


class Post(models.Model):
    title = models.CharField(max_length=255)
    renovaters = models.ForeignKey(User, models.PROTECT)
    date = models.DateField()
    eventType = models.CharField(max_length=255) 
    location = models.CharField(max_length=255)
    peopleCount = models.IntegerField()
    # choice here 
    ageProfolio = models.CharField(max_length=255)
    kitchenType = models.CharField(max_length=255)
    provideCookery = models.BooleanField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    extraCriteria = models.ManyToManyField(Criteria)
    # choice here
    state = models.CharField(max_length=255)



class Taker(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    bidder = models.ForeignKey(User, models.PROTECT)
    offer = models.DecimalField(max_digits=12, decimal_places=2)