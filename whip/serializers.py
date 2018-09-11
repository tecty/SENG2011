from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import Parameter, Post, Bid
from django.utils import timezone

# serializer of user models
# validators.UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # password only can be written 
    password = serializers.CharField(write_only = True)
    # also the password again
    password_again = serializers.CharField(write_only = True)

    """
    validation codes  
    """

    def validate(self, data):
        if data["password"] != data["password_again"]:
            raise serializers.ValidationError({
                "password_again":[
                    "Two password must be same"
                ]
            })

        # ELSE: validate successfully 
        return data

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            "password",
            "password_again",'email',
            'is_staff'
        )

    def create(self,validated_data):
        user = super(UserSerializer, self).create(validated_data)
        # # set the password with encryption 
        # user.set_password(validated_data['password'])
        # user.save()
        return user



class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        # fields = ('key', 'value', "isDelete")
        fields = ('id','key', 'value')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    # protect the state been modify by client 
    # TODO: Provide another to endpoint to change it 
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
        # created and save the bid bid  
        bid = super(BidSerializer,self),create(validated_data)
        return bid



class PostSerializer(serializers.ModelSerializer):
    # set the foreign stat sytle
    # extraParameter =serializers.StringRelatedField(many = True)
    state  = serializers.CharField(read_only = True)
    bid_set = BidSerializer(many=True,read_only = True)
    
    
    poster = UserSerializer(read_only = True)

    """
    validation code of this serializer
    """
    def validate_extraParameter(self, extraParameter):
        """
        for the mutual exclusion of keys in extraparameter
        
        If there is a duplicate keys in extra paramter, raise error 
        """

        # create a dict to detect collesion  
        ParameterDict = {}

        for Parameter in extraParameter:
            # perform a check for duplicate key in the dictionary 
            if Parameter.key in  ParameterDict:
                # raise a validate error and break the loop
                raise serializers.ValidationError(
                    "extraParameter must have unique key"
                )
            # add this key value pair into this dict
            # so it will raise error when it occour a duplicate key
            ParameterDict[Parameter.key] = Parameter.value
        # ELSE: validate successfully return back this data to validated_data 
        return extraParameter 

    def validate_eventTime(self, eventTime):
        """ Event time > now """
        if eventTime <= timezone.now():
            raise serializers.ValidationError(
                "Event Time must be later than now;"
            )
        return eventTime

    def validate_bidClossingTime(self, bidClossingTime):
        """ Bid clossing time > now """
        if bidClossingTime <= timezone.now():
            raise serializers.ValidationError(
                "Bid Clossing Time must be later than now;"
            )
        return bidClossingTime

    def validate(self,data):
        if data["bidClossingTime"] >= data["eventTime"]:
            raise serializers.ValidationError(
                {"bidClossingTime":[
                    "Bid Clossing must happen before the Event time "
                ]}
            )
        # ELSE: validate successfully 
        return data

    class Meta:
        model = Post
        fields = (
            "id",
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
        # push back the current defult user 
        validated_data['poster'] = self.context['request'].user

        # use parents method to create this obj
        post = super(PostSerializer,self).create(validated_data)

        # return back this created obj
        return post 



