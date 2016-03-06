from django.db import models
from language.models import LangTranslation, LanguageDef

# providerprofile app

class Provider(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    skill = models.ForeignKey(Skill)
    category = models.ForeignKey(Category)

class Skill(models.Model):
    skillDef = models.ForeignKey(SkillDef)

class UndefinedSkill(models.Model):
    undefinedSkill = models.ForeignKey(LangTranslation)
    languageDef = models.ForeignKey(LanguageDef)

class SkillDef(models.Model):
    skill = models.ForeignKey(LangTranslation)

class Category(models.Model):
    categoryDef = models.ForeignKey(categoryDef)

class CategoryDef(models.Model):
    category = models.ForeignKey(LangTranslation)

class Title(models.Model):
    title = models.CharField(max_length=50)
    bkgd = models.CharField(max_length=1)
