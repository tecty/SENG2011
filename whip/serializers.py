from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Parameter, Post, Bid

# serializer of user models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        # fields = ('key', 'value', "isDelete")
        fields = ('key', 'value')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    bidder = UserSerializer(read_only = True)
    class Meta:
        model = Bid
        fields = ('post', 'bidder', 'offer', "state")


class PostSerializer(serializers.ModelSerializer):
    # set the foreign stat sytle
    # extraParameter =serializers.StringRelatedField(many = True)
    bid_set = BidSerializer(many=True,read_only = True)
    poster = UserSerializer(read_only = True)

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
            "extraParameter",
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
        extraParameter = validated_data.pop("extraParameter")

        # print("imhere")
        # print(extraParameter)

        # create a dict to prevent collesion 
        ParameterDict = {}

        for Parameter in extraParameter:
            # perform a check for duplicate key in the dictionary 
            if Parameter.key in  ParameterDict:
                # raise a validate error 
                raise serializers.ValidationError(
                    "Parameter must have unique key"
                )
            ParameterDict[Parameter.key] = Parameter.value

        # push back the Data (Many to many couldn't push back )
        # validated_data["title"] = title
        
        ret = Post.objects.create(**validated_data)

        # for Parameter in extraParameter:
        ret.extraParameter.set(extraParameter)

        return ret 



