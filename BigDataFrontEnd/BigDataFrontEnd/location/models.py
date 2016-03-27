from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

# location app

#TIMEZONES = pytz.common_timezones_set

class AdminDiv(models.Model):
    pass

class Country(models.Model):
    pass

class AdminDivDef(models.Model):
    adminDiv = models.ForeignKey(AdminDiv)

    languageCode = models.CharField(max_length=2)
    adminDivDef = models.CharField(max_length=50)

class CountryDef(models.Model):
    country = models.ForeignKey(Country)

    languageCode = models.CharField(max_length=2)
    countryDef = models.CharField(max_length=50)

class Location(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    timeZone = models.CharField(max_length=100, blank=True, null=True)
    adminDiv = models.ForeignKey(AdminDiv, blank=True, null=True)
    country = models.ForeignKey(Country)