from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Criteria, Post, Bid

# serializer of user models
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class CriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criteria
        fields = ('key','value',"isDelete")

class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid 
        fields = ('post','bidder','offer',"state")
    
class PostSerializer(serializers.HyperlinkedModelSerializer):
    # set the foreign stat sytle 
    # extraCriteria =CriteriaSerializer(many = True,read_only = True)
    # bids = BidSerializer(many = True, read_only = True)
    bid = BidSerializer(many = True,read_only = True)
    
    class Meta:
        model = Post
        fields = (
                "title",
                "msg",
                "poster",
                "evenTime",
                "bidClossingTime",
                "location",
                "peopleCount",
                "budget",
                "state",
                "bid",
                "extraCriteria",
            )


