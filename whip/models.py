from django.db import models
from django.contrib.auth.models import User 

# for handling signal of user model
# this will extend the user model 
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Location code copy from my own GitHub
https://github.com/tecty/SENG2021/blob/master/backend/post/models.py
"""
class Location(models.Model):
    # the exact name for that location
    address = models.CharField(max_length = 512,blank=True)
    # record the precise location of that location
    # has number before point is 15-12 = 3, after the point is 20
    lat = models.DecimalField(max_digits=24, decimal_places= 20)
    lng = models.DecimalField(max_digits=24, decimal_places= 20)


"""
Extention of Current User model of Django 
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Location will be change to foreign key 
    location =  models.ForeignKey(Location,models.PROTECT,blank = True, null = True)
    # telephone of this customer 
    tel = models.BigIntegerField(null= True)
    # Whether is trusted by out group (admin manage )
    is_trusted = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Message(models.Model):
    # Support the disscussion 
    parentMsg = models.ForeignKey("self",on_delete= models.CASCADE)
    # this message  
    msg = models.CharField(max_length = 1024)
    

class Parameter(models.Model):
    key = models.CharField(max_length = 255)
    value = models.CharField(max_length = 1024)
    # soft delete the Parameter 
    isDelete = models.BooleanField(default=False)
    # functions used to show the object's name in Django 
    def __unicode__(self):
        return "%s : %s" % (self.key, self.value)
    def __str__(self):
        return self.__unicode__()


class Event(models.Model):
    # basic description of this event 
    title = models.CharField(max_length=255)
    # message foreign key to support discussion 
    msg = models.ForeignKey(Message,on_delete= models.PROTECT)
    # who post this event 
    poster = models.ForeignKey(User, models.PROTECT)
    # the time this event will be held 
    eventTime = models.DateTimeField()
    # the time need to close the bid 
    bidClosingTime = models.DateTimeField()
    # where is the event
    location =  models.ForeignKey(Location,models.PROTECT)

class Post(models.Model):
    # basic description of this event 
    title = models.CharField(max_length=255)
    # message foreign key to support discussion 
    msg = models.ForeignKey(Message,on_delete= models.PROTECT)
    # who post this event 
    poster = models.ForeignKey(User, models.PROTECT)
    # the time this event will be held 
    eventTime = models.DateTimeField()
    # the time need to close the bid 
    bidClosingTime = models.DateTimeField()
    # where is the event
    location =  models.ForeignKey(Location,models.PROTECT)
    # how many people will occour 
    peopleCount = models.IntegerField()
    # the budget of whole event 
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    # how much points received by bidder
    posterReceivedPoints = models.IntegerField(default= 0)
    # state of the event 
    state = models.CharField(
        max_length=2,
        choices = (
            ('BD','Bidding'),
            ('DL','Deal'),
            ('FN','Finished'),
            ('CL','Canceled'),
        ),
        default = 'BD',
    )
    # not required Parameter is added by relation of 
    # Parameter table 
    extraParameter = models.ManyToManyField(
        Parameter,
        blank = True,
        related_name = "extra_parameter"
    )

    # extra key for non neccessary one to many relationship 
    event = models.ForeignKey(Event,on_delete = models.CASCADE, blank = True ,null= True)

    # functions used to show the object's name in Django 
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.__unicode__()

class Bid(models.Model):
    # which post is this bid for 
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    # A message to have better chance to win
    # foreign key to msg to support discussion 
    msg = models.ForeignKey(Message, on_delete = models.PROTECT)
    # state of this event 
    state = models.CharField(
        max_length=2,
        choices = (
            ('BD','Bidding'),
            ('SD','Selected'),
            ('US','Unselected'),
            ('FN','Finished'),
            ('CL','Canceled'),
        ),
        default = 'BD',
    )
    # who bid this  
    bidder = models.ForeignKey(User, models.PROTECT)
    # what the prive this bidder offer 
    offer = models.DecimalField(max_digits=12, decimal_places=2)
    # How much did bidder received 
    bidderReceivedPoints = models.IntegerField(default= 0) 

    # functions used to show the object's name in Django 
    def __unicode__(self):
        return "%s bids %s" % (self.bidder, self.offer)
    def __str__(self):
        return self.__unicode__()

