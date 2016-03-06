from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from language.models import Language

# user app

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    email2 = models.EmailField()
    bio = models.CharField(max_length=400)
    isProvider = models.BooleanField(default=False)
    isClient = models.BooleanField(default=False)

class Feedback(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    language = models.ForeignKey(Language)
    feedback = models.CharField(max_length=400)
    rate = models.IntegerField()
    bkgd = models.CharField(max_length=1)

class RateAgg(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    ProviderRateAgg = models.DecimalField(max_digits=3, decimal_places=2)
    ClientRateAgg = models.DecimalField(max_digits=3, decimal_places=2)

class Title(models.Model):
    title = models.CharField(max_length=50)
    bkgd = models.CharField(max_length=1)


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