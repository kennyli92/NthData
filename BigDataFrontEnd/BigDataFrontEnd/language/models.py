from django.db import models
from django.contrib.auth.models import User

# language app

class LanguageDef(models.Model):
    # Other fields here
    languageName = models.CharField(max_length=20)
    langAbbr = models.CharField(max_length=10)

class Language(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Gets language string from LanguageDef table
    languageDef = models.ForeignKey(LanguageDef)

class LangTranslation(models.Model):
    # Other fields here
    note = models.CharField(max_length=255, null=True, blank=True)
    text_EN = models.CharField(max_length=255)


