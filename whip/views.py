from django.shortcuts import render
from .serializers import UserSerializer, User, \
    Post, PostSerializer, \
    Parameter, ParameterSerializer, \
    Bid, BidSerializer,\
    Location, LocationSerializer,\
    Message, MessageSerializer,\
    Event, EventSerializer
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework.decorators import action


# Own premission  
from .permission import GuestCreateOnly,OwnerUpdateOnly,IsAdminOrReadOnly

class LocationViewset(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # only for test use 
    # permission_classes = [permissions.AllowAny]
    
    permission_classes = [GuestCreateOnly,OwnerUpdateOnly]


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    permission_classes = [IsAdminOrReadOnly]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    @action(detail = True, methods = ['POST'], url_name='Rate-Poster')
    def rate(self, request,pk= None):
        # get the post object from the pk specified 
        bid = self.get_object()
        # use a method in object to choose the bidder 
        bid.rate(request.data["rate"])

        # wrap the serializer and with this bid detail 
        serializer = self.get_serializer(bid)

        # return back this bid detail 
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
    """
    TODO: need to prevent mutiple time state change
    """

    @action(detail = True, methods = ['POST'], url_name='Choose Bidder')
    def choose(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.choose(request.data["id"])

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data)



    @action(detail = True, methods = ['POST','GET'], url_name='Finish Post')
    def finish(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.finish()

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data)

    @action(detail = True, methods = ['POST'], url_name='Rate-Bidder')
    def rate(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.rate(request.data["rate"])

        # wrap the serializer and with this post detail 
        serializer = self.get_serializer(post)

        # return back this post detail 
        return Response(serializer.data)