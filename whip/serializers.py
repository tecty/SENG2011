from django.contrib.auth.models import User
from rest_framework import serializers


# serializer of user models
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            "renovaters" ,
            "date" ,
            "eventType" ,
            "location" ,
            "peopleCount" ,
            "ageProfolio" ,
            "kitchenType" ,
            "provideCookery" ,
            "budget" ,
            "extraCriteria",
            "state"
        )

class CriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criteria
        fields = ('key','value')

class TakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Taker 
        fields = ('post','bidder','offer')