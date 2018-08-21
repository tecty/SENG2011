from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Criteria(models.Model):
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1024)
    # soft delete the criteria 
    isDelete = models.BooleanField(default=False)

    # functions used to show the object's name in Django 
    def __unicode__(self):
        return "%s : %s" % (self.key, self.value)
    def __str__(self):
        return self.__unicode__()

class Post(models.Model):
    # basic description of this event 
    title = models.CharField(max_length=255)
    msg = models.CharField(max_length=1024, blank=True)
    # who post this event 
    poster = models.ForeignKey(User, models.PROTECT)
    # the time this event will be held 
    evenTime = models.DateTimeField()
    # the time need to close the bid 
    bidClossingTime = models.DateTimeField()
    # where is the event
    location = models.CharField(max_length=255)
    # how many people will occour 
    peopleCount = models.IntegerField()
    # the budget of whole event 
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    # state of the event 
    state = models.CharField(max_length=255)
    # not required criteria is added by relation of 
    # Criteria table 
    extraCriteria = models.ManyToManyField(Criteria,blank = True)

    # functions used to show the object's name in Django 
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.__unicode__()

class Bid(models.Model):
    # which post is this bid for 
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    # A message to have better chance to win
    msg = models.CharField(max_length = 1024)
    # state of this event 
    state = models.CharField(max_length=255)
    # who bid this  
    bidder = models.ForeignKey(User, models.PROTECT)
    # what the prive this bidder offer 
    offer = models.DecimalField(max_digits=12, decimal_places=2)
    
    # functions used to show the object's name in Django 
    def __unicode__(self):
        return "%s bids %s" % (self.bidder, self.offer)
    def __str__(self):
        return self.__unicode__()