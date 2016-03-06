from django.db import models
from language.models import LangTranslation
from django.utils import timezone
import pytz

# location app

TIMEZONES = pytz.common_timezones

class AdminDivDef(models.Model):
    adminDef = models.ForeignKey(LangTranslation)
    name = models.ForeignKey(LangTranslation)

class CountryDef(models.Model):
    country = models.ForeignKey(LangTranslation)

class Location(models.Model):
    timeZone = models.CharField(max_length=100, blank=True, null=True, choices=TIMEZONES)
    adminDivDef = models.ForeignKey(AdminDivDef)
    countryDef = models.ForeignKey(CountryDef)