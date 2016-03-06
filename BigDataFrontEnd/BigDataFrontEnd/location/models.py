from django.db import models
from language.models import LangTranslation
from django.contrib.auth.models import User
from django.utils import timezone
import pytz

# location app

TIMEZONES = pytz.common_timezones_set

class AdminDivDef(models.Model):
    adminDivDef = models.ForeignKey(LangTranslation)
    #name = models.ForeignKey(LangTranslation)

class CountryDef(models.Model):
    country = models.ForeignKey(LangTranslation)

class Location(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    #timeZone = models.CharField(max_length=100, blank=True, null=True, choices=TIMEZONES)
    adminDivDef = models.ForeignKey(AdminDivDef)
    countryDef = models.ForeignKey(CountryDef)