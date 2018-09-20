# This file cannot run standalone 
# Must be called by init_db.sh 
from django.contrib.auth.models import Group,Permission
from itertools import chain

"""
dividing two groups of user here
- Set it's name
- Clearify it's premission
"""
# bidder group 
bidder = Group.objects.create(name = "Bidder")

permission_list = \
list(
  chain(
    Permission.objects.filter(content_type__model = "event"),
    Permission.objects.filter(content_type__model = "post"),
    Permission.objects.filter(content_type__model = "message")
  )
)



# CRUD of post Event Msg 
bidder.permissions.set(permission_list)
# save the setting 
bidder.save()

# poster group 
poster = Group.objects.create(name = "Poster")
permission_list = list(
  chain(
    Permission.objects.filter(content_type__model = "bid"),
    Permission.objects.filter(content_type__model = "message")
  )
)

# CRUD of post Event Msg 
poster.permissions.set(permission_list)
# save the setting 
poster.save()
