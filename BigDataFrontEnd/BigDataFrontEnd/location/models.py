from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

# location app

#TIMEZONES = pytz.common_timezones_set
class AdminDivDef(models.Model):
    pass

class CountryDef(models.Model):
    pass

class AdminDivDefTr(models.Model):
    adminDivDef = models.ForeignKey(AdminDivDef)

    languageCode = models.CharField(max_length=2)
    adminDiv = models.CharField(max_length=50)

class CountryDefTr(models.Model):
    countryDef = models.ForeignKey(CountryDef)

    languageCode = models.CharField(max_length=2)
    country = models.CharField(max_length=50)

class Location(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    timeZone = models.CharField(max_length=100, blank=True, null=True)
    adminDivDef = models.ForeignKey(AdminDivDef, blank=True, null=True)
    countryDef = models.ForeignKey(CountryDef, blank=True, null=True)