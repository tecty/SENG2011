from rest_framework import permissions

"""
permission classes for party whip 
"""

class GuestCreateOnly(permissions.BasePermission):
    # admin manage is not provided via apis
    message = "User can only be created by guest"

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            if request.method == "POST":
                # only guest can create,
                return True
        # no thing can allowed to prevent data leak 
        return False
            
class OwnerUpdateOnly(permissions.BasePermission):
    """Object premission method"""
    message = "You're not the owner of this account"

    def has_object_permission(self, request, view,obj):
        if request.user and request.user.is_authenticated:
            # here is a logined user 
            if request.user == obj:
                # a user can change his data 
                return True
        # auth fail
        return False