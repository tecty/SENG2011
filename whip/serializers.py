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
        # fields = ('key', 'value', "isDelete")
        fields = ('key', 'value')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid
        fields = ('post', 'bidder', 'offer', "state")


class PostSerializer(serializers.ModelSerializer):
    # set the foreign stat sytle
    extraCriteria =CriteriaSerializer(many = True,read_only = True)
    bid_set = BidSerializer(many=True,read_only = True)
    poster = serializers.StringRelatedField()

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
            "bid_set",
            "extraCriteria",
        )

    def create(self, validated_data):
        # Pop the data we want to verify 

        # title = validated_data.pop("title")
        # msg = validated_data.pop("msg")
        # poster = validated_data.pop("poster")
        # evenTime = validated_data.pop("evenTime")
        # bidClossingTime = validated_data.pop("bidClossingTime")
        # location = validated_data.pop("location")
        # peopleCount = validated_data.pop("peopleCount")
        # budget = validated_data.pop("budget")
        # state = validated_data.pop("state")
        extraCriteria = validated_data.pop("extraCriteria")

        # print("imhere")
        # print(extraCriteria)

        # create a dict to prevent collesion 
        criteriaDict = {}

        for criteria in extraCriteria:
            # perform a check for duplicate key in the dictionary 
            if criteria.key in  criteriaDict:
                # raise a validate error 
                raise serializers.ValidationError(
                    "Criteria must have unique key"
                )
            criteriaDict[criteria.key] = criteria.value

        # push back the Data (Many to many couldn't push back )
        # validated_data["title"] = title
        
        ret = Post.objects.create(**validated_data)

        # for criteria in extraCriteria:
        ret.extraCriteria.set(extraCriteria)

        return ret 



