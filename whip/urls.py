from django.conf.urls import url, include
from .views import UserViewSet,PostViewSet, ParameterViewSet, BidViewSet
from rest_framework import routers

# the urls in this app 
# create a router 
router = routers.DefaultRouter()
# register viewset to router
router.register(r'users', UserViewSet)
router.register("posts", PostViewSet )
router.register("Parameters", ParameterViewSet )
router.register("bids", BidViewSet )


# the url pattern for django 
urlpatterns = [
    # register the router to django 
    url(r'^', include(router.urls)),
]