from django.contrib.auth.models import User,Group
from rest_framework import serializers,validators
from .models import Location, Profile, Parameter, Post, Bid,Event,Message
from django.utils import timezone

# to support the recursive message 
from rest_framework_recursive.fields import RecursiveField

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("address","lat","lng")
    def create(self,validated_data):
        # Only create a location if it's exist  
        return Location.objects.get_or_create(**validated_data)[0]

"""
Solution in 
https://django-rest-auth.readthedocs.io/en/latest/faq.html
And this serialiser to simply the saving procedure, never have direct use in 
viewset
"""
class ProfileSerializer(serializers.ModelSerializer):
    # couldn't be changed by user 
    is_trusted = serializers.BooleanField(read_only = True)
    class Meta: 
        model = Profile
        fields = (
            "location",
            "tel",
            "is_trusted",
        )




class UserSerializer(serializers.HyperlinkedModelSerializer):
    # password only can be written 
    password = serializers.CharField(write_only = True)
    # also the password again
    password_again = serializers.CharField(write_only = True)

    """
    Extended Fields
    """
    # location of this user 
    location = LocationSerializer(source = "profile.location")
    # telephone of this user
    tel = serializers.IntegerField(source = "profile.tel")
    # whether it is is the  trusted 
    is_trusted = serializers.BooleanField(
        source = "profile.is_trusted", read_only = True)

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
        # we no longer need the password again
        data.pop("password_again")
        # ELSE: validate successfully 
        return data

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            "password",
            "password_again",
            # email somtime will trigger some wired behaviour
            # not using it at this request stage
            # 'email',
            # we don't need the staff info, and we shouldn't change it at frontend 
            # 'is_staff', 
            "location",
            "tel",
            "is_trusted",
        )

    def update(self, validated_data):
        # do the same things as create 
        # pop the foreign to create instance 
        profile_data = validated_data.pop("profile",{})

        # I don't know the ** means
        # This line just for creating a location instance 
        # if there is not exists  
        # [0] is for that we only need the object from this creation
        location = Location.objects.get_or_create(
            **(profile_data.pop("location")))[0]

        # push back the location object 
        profile_data['location'] = location
        # create this user 
        user = super(UserSerializer, self).update(validated_data)

        # user profile_data serializer to update 
        ProfileSerializer().update(user.profile,validated_data=profile_data)

        return user

    def create(self,validated_data):
        # pop the foreign to create instance 
        profile_data = validated_data.pop("profile",{})

        # I don't know the ** means
        # This line just for creating a location instance 
        # if there is not exists  
        # [0] is for that we only need the object from this creation
        location = Location.objects.get_or_create(
            **(profile_data.pop("location")))[0]

        # push back the location object 
        profile_data['location'] = location

        # create this user 
        user = super(UserSerializer, self).create(validated_data)

        # TODO: need to modify if we divide our group data 
        user.groups.add(Group.objects.get(name='Poster'))
        user.groups.add(Group.objects.get(name='Bidder'))


        # set the password by a delicate function 
        # In this way, the password will encrypt and save correctly
        user.set_password(validated_data["password"])
        # save this model 
        user.save()

        # user profile_data serializer to update 
        ProfileSerializer().update(user.profile,validated_data=profile_data)
        
        return user
    
class MessageSerializer(serializers.ModelSerializer):
    parentMsg = serializers.CharField(write_only = True,allow_blank = True)
    sub_msg = serializers.ListField(child = RecursiveField(),source= "message_set.all",read_only = True)
    owner = UserSerializer(read_only = True)
    msg = serializers.CharField(allow_null = True)
    class Meta:
        model = Message
        fields = (
            "id",
            "parentMsg",
            "msg",
            "owner",
            "sub_msg"
        )

    def create(self, validated_data):
        # push this user to validated data 
        validated_data['owner'] =  self.context['request'].user

        # pop the parent message first 
        parentMsg = validated_data.pop("parentMsg","")
        if parentMsg:
            # re push in the fetched instance of parentMsg for the forein link 
            validated_data["parentMsg"] = Message.objects.get(pk = parentMsg)
        
        # call the super method to create this obj
        return super(MessageSerializer,self).create(validated_data)


class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only = True)
    location = LocationSerializer()

    """
    validation code of this serializer
    """
    def validate_eventTime(self, eventTime):
        """ Event time > now """
        if eventTime <= timezone.now():
            raise serializers.ValidationError(
                "Event Time must be later than now;"
            )
        return eventTime

    def validate_bidClosingTime(self, bidClosingTime):
        """ Bid closing time > now """
        if bidClosingTime <= timezone.now():
            raise serializers.ValidationError(
                "Bid Closing Time must be later than now;"
            )
        return bidClosingTime

    def validate(self,data):
        if data["bidClosingTime"] >= data["eventTime"]:
            raise serializers.ValidationError(
                {"bidClosingTime":[
                    "Bid Closing must happen before the Event time "
                ]}
            )
        # ELSE: validate successfully 
        return data

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "owner",
            "eventTime",
            "bidClosingTime",
            "location"
        )
    
    def create(self,validated_data):
        validated_data['owner'] = self.context['request'].user

        #  location data may not exist 
        location = validated_data.pop("location",{})
        # get or create a location 
        validated_data["location"] = \
            LocationSerializer().create(location)

        # use parents method to create this obj
        post = super(EventSerializer,self).create(validated_data)

        # return back this created obj
        return post 



class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        # fields = ('key', 'value', "isDelete")
        fields = ('id','key', 'value')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    # protect the state been modify by client 
    # TODO: Provide another to endpoint to change it 
    state  = serializers.CharField(read_only = True)
    post = serializers.PrimaryKeyRelatedField(queryset =  Post.objects.all())
    owner = UserSerializer(
        read_only = True,
    )
        # inherentant the context fcfrom this class 
    msg = MessageSerializer(read_only = True)

    message = serializers.CharField(write_only = True)

    class Meta:
        model = Bid
        fields = (
            'id',
            'post',
            'owner',
            'msg',
            'message',
            'offer',
            "state","bidderReceivedPoints"
        )

    def create(self, validated_data):
        # push the current user into the validate data 
        validated_data['owner'] =  self.context['request'].user

        # pop the message to create the message char 
        msg =  validated_data.pop('message',
            {})
        # pass this message as string to it 
        validated_data['msg'] = \
            MessageSerializer(context = self.context ).create({"msg": msg})
        
        # created and save the bid bid  
        bid = super(BidSerializer,self).create(validated_data)
        return bid



class PostSerializer(serializers.ModelSerializer):
    eventId = serializers.IntegerField(write_only = True)
    event = EventSerializer(read_only = True)
    # set the foreign stat sytle
    # extraParameter =serializers.StringRelatedField(many = True)
    state  = serializers.CharField(read_only = True)
    bid_set = BidSerializer(many=True,read_only = True)

    posterReceivedPoints =serializers.IntegerField(read_only = True)

    # inherentant the context fcfrom this class 
    msg = MessageSerializer(read_only = True)

    message = serializers.CharField(write_only = True)

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

    class Meta:
        model = Post
        fields = (
            "eventId",
            "event",
            "peopleCount",
            "budget",
            "posterReceivedPoints",
            "state",
            "extraParameter",
            "msg",
            "message",
            "bid_set",
        )

    def create(self, validated_data):
        # one line to pop the event id and fetch the event object
        # then attach the event to this post 
        validated_data["event"] = \
            Event.objects.get(pk = validated_data.pop("eventId"))



        # pop the message to create the message char 
        msg =  validated_data.pop('message',{})
        # pass this message as string to it 
        validated_data['msg'] = \
            MessageSerializer(context = self.context ).create({"msg": msg})



        # use parents method to create this obj
        post = super(PostSerializer,self).create(validated_data)

        # return back this created obj
        return post 