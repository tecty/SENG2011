from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import Parameter, Post, Bid
from django.utils import timezone

# serializer of user models
# validators.UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        # fields = ('key', 'value', "isDelete")
        fields = ('id','key', 'value')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    # protect the state been modify by client 
    # TODO: Provide another to post and change it 
    state  = serializers.CharField(read_only = True)
    bidder = UserSerializer(
        read_only = True,
        # default = serializers.CurrentUserDefault()  
    )
    class Meta:
        model = Bid
        fields = ('post', 'bidder', 'offer', "state")

    def create(self, validated_data):
        # push the current user into the validate data 
        validated_data['bidder'] =  self.context['request'].user
        # return the created bid  
        return Bid.objects.create(**validated_data)



class PostSerializer(serializers.ModelSerializer):
    # set the foreign stat sytle
    # extraParameter =serializers.StringRelatedField(many = True)
    state  = serializers.CharField(read_only = True)
    bid_set = BidSerializer(many=True,read_only = True)
    poster = UserSerializer(
        read_only = True
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "msg",
            "poster",
            "eventTime",
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
        eventTime = validated_data.pop("eventTime")
        bidClossingTime = validated_data.pop("bidClossingTime")
        # location = validated_data.pop("location")
        # peopleCount = validated_data.pop("peopleCount")
        # budget = validated_data.pop("budget")
        # state = validated_data.pop("state")
        extraParameter = validated_data.pop("extraParameter")

        if bidClossingTime >= eventTime:
            raise serializers.ValidationError(
                {"bidClossingTime":[
                    "Bid Clossing Time must be before the Event time "
                ]}
            )
        if eventTime <= timezone.now():
            raise serializers.ValidationError(
                {"eventTime":[
                    "Event Time must be later time now;"
                ]}
            )
        if bidClossingTime <= timezone.now():
            raise serializers.ValidationError(
                {"bidClossingTime":[
                    "Bid Clossing Time must be later time now;"
                ]}
            )

        # print(extraParameter)

        # create a dict to prevent collesion 
        ParameterDict = {}

        for Parameter in extraParameter:
            # perform a check for duplicate key in the dictionary 
            if Parameter.key in  ParameterDict:
                # raise a validate error 
                raise serializers.ValidationError(
                    {"Parameter":
                        ["Parameter must have unique key"]
                    }
                )
            ParameterDict[Parameter.key] = Parameter.value

        # push back the Data (Many to many couldn't push back )
        validated_data["eventTime"] = eventTime
        validated_data["bidClossingTime"] = bidClossingTime
        
        # push back the current defult user 
        validated_data['poster'] = self.context['request'].user

        # create the new instance of this post  
        ret = Post.objects.create(**validated_data)

        # for Parameter in extraParameter:
        ret.extraParameter.set(extraParameter)

        return ret 



