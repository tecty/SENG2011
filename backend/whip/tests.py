from django.test import TestCase
from .models import *
from django.utils import timezone
import datetime


# Create your tests here.

class BidderMarkTest(TestCase):
  def setUp(self):
    """Create a list of User to be test environment"""
    self.user001 =User.objects.create_user('u001',"u001@example.cn","tt")
    self.user002 =User.objects.create_user('u002',"u002@example.cn","tt")
    self.user003 =User.objects.create_user('u003',"u003@example.cn","tt")
    self.user004 =User.objects.create_user('u004',"u004@example.cn","tt")

    self.user_list = [
      self.user001,
      self.user002,
      self.user003,
      self.user004,
    ]

  def test_0_bidds(self):
    theEvent = Event.objects.create(
      title = "sth",
      owner = self.user_list[0],
      eventTime =timezone.now(),
      bidClosingTime = timezone.now()
    )
    thePost = Post.objects.create(
      event = theEvent,
      title = "missing",
      peopleCount = 10,
      budget = 100
    )
    thePost.bid_set.create(
      owner = self.user_list[1],
      offer = 100
    )
