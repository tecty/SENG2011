"""PartyWhip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# import jwt auth 
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # the endpoint for admin site
    path('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),

    # register api authentication from rest framework 
    url(r'^api-auth/', 
        include('rest_framework.urls', namespace='rest_framework')),

    # jwt auth
    url(r'^api-token-auth/', obtain_jwt_token),


    #  include the url from whip app 
    path('api-v0/',include('whip.urls')),

    # bind another end point to api-v0 for convinence 
    url(r'^api-v0/api-token-auth/', obtain_jwt_token),

]
