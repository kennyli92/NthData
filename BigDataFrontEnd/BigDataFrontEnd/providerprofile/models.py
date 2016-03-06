from django.db import models
from language.models import LangTranslation, LanguageDef
from user.models import Title
from django.contrib.auth.models import User

# providerprofile app
class CategoryDef(models.Model):
    categoryDef = models.ForeignKey(LangTranslation)

class SkillDef(models.Model):
    skillDef = models.ForeignKey(LangTranslation)

class Skill(models.Model):
    skill = models.ForeignKey(SkillDef)

class UndefinedSkill(models.Model):
    undefinedSkill = models.ForeignKey(LangTranslation)
    languageDef = models.ForeignKey(LanguageDef)

class Category(models.Model):
    category = models.ForeignKey(CategoryDef)

class Provider(models.Model):
# This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    skill = models.ForeignKey(Skill)
    category = models.ForeignKey(Category)
    title = models.ForeignKey(Title)
