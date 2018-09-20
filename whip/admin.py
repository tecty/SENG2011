from django.contrib import admin
from .models import \
Location, Profile, Message, Parameter, Event, Post, Bid

admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Parameter)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Bid)