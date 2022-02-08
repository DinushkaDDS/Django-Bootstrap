from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        # if request has HTTP verbs included in SAFE_METHODS–a tuple containing GET, OPTIONS, and HEAD–then,
        #    it is a read-only request and permission is granted
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user