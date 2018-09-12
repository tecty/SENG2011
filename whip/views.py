from django.shortcuts import render
from .serializers import UserSerializer, User, \
    Post, PostSerializer, \
    Parameter, ParameterSerializer, \
    Bid, BidSerializer
from rest_framework import viewsets

from rest_framework import permissions


# Own premission  
from .permission import GuestCreateOnly,OwnerUpdateOnly


# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [GuestCreateOnly,OwnerUpdateOnly]


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
