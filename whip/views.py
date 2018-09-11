from django.shortcuts import render
from .serializers import UserSerializer, User, \
    Post, PostSerializer, \
    Parameter, ParameterSerializer, \
    Bid, BidSerializer
from rest_framework import viewsets


# import premission for the premission rewrite 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
# import the rest response to create our own response 
from rest_framework.response import Response



# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [AllowAny]    

    # @api_view(['POST'])
    # @permission_classes((AllowAny,))
    # def create_user(self,request):
    #     serialized = UserSerializer(data=request.data)
    #     if serialized.is_valid():
    #         serialized.save()
    #         return Response(serialized.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
