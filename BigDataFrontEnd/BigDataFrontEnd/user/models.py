from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    email2 = models.EmailField()
    bio = models.CharField(max_length=400)
    isProvider = models.BooleanField(default=False)
    isClient = models.BooleanField(default=False)

#class Location(models.Model):
#    # This field is required.
#    user = models.OneToOneField(User)

#    # Other fields here
#    language = models.CharField(

def assure_user_profile_exists(pk):
    
    #Creates a user profile if a User exists, but the
    #profile does not exist.  Use this in views or other
    #places where you don't have the user object but have the pk.
    
    user = User.objects.get(pk=pk)
    try:
        # fails if it doesn't exist
        userprofile = user.userprofile
    except UserProfile.DoesNotExist:
        userprofile = UserProfile(user=user)
        userprofile.save()
    return


def create_user_profile(**kwargs):
    UserProfile.objects.get_or_create(user=kwargs['user'])