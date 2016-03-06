from django.db import models
from language.models import LangTranslation

# clientprofile app

class Client(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    organization = models.ForeignKey(Organization)

class Organization(models.Model):
    name = models.ForeignKey(LangTranslation)
