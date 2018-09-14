from django.shortcuts import render
from .serializers import UserSerializer, User, \
    Post, PostSerializer, \
    Parameter, ParameterSerializer, \
    Bid, BidSerializer,\
    Location, LocationSerializer,\
    Message, MessageSerializer
from rest_framework import viewsets,permissions
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


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    

    @action(detail = True, methods = ['POST','GET'], url_name='Choose Bidder')
    def choose(self, request,pk= None):
        # get the post object from the pk specified 
        post = self.get_object()
        # use a method in object to choose the bidder 
        post.choose( request.data["id"])

        # return back this post detail 
        return post 
