# This file cannot run standalone 
# Must be called by init_db.sh 
from django.contrib.auth.models import Group,Permission

"""
dividing two groups of user here
- Set it's name
- Clearify it's premission
"""
# bidder group 
bidder = Group.objects.create(name = "Bidder")
# CRUD of post Event Msg 
bidder.objects.permissions_set(
  Permission.objects.filter(
    content_type__model__contains = "event" 
  )
)
bidder.permissions_set(
  Permission.objects.filter(
    content_type__model__contains = "post" 
  )
)
bidder.permissions_set(
  Permission.objects.filter(
    content_type__model__contains = "msg" 
  )
)
# save the setting 
bidder.save()

# poster group 
poster = Group.objects.create(name = "Poster")
# CRUD of post Event Msg 
poster.permissions_set(
  Permission.objects.filter(
    content_type__model__contains = "bid" 
  )
)
poster.permissions_set(
  Permission.objects.filter(
    content_type__model__contains = "msg" 
  )
)
# save the setting 
poster.save()
