from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# user app

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    email2 = models.EmailField()
    isProvider = models.BooleanField(default=False)
    isClient = models.BooleanField(default=False)

class UserProfileTr(models.Model): 
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    bioC = models.CharField(max_length=400)
    bioP = models.CharField(max_length=400)

class RateAgg(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    ProviderRateAgg = models.DecimalField(max_digits=3, decimal_places=2)
    ClientRateAgg = models.DecimalField(max_digits=3, decimal_places=2)

class Category(models.Model):
    pass

class CategoryDef(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    categoryName = models.CharField(max_length=50)

# -------- providerprofile tables (placed in user.models due to circular dependencies, can't compile otherwise) --------
class Skill(models.Model):
    pass

class SkillDef(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    skillName = models.CharField(max_length=50)

#temp table. Create new standard skill name for Skill table.
class UndefinedSkill(models.Model):
    languageCode = models.CharField(max_length=2)
    undefinedSkill = models.CharField(max_length=50)

class Provider(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category)
    skill = models.ForeignKey(Skill)
    undefinedSkill = models.ForeignKey(UndefinedSkill)

# -------- end providerprofile --------

# -------- clientprofile tables (placed in user.models due to circular dependencies, can't compile otherwise) --------
class Organization(models.Model):
    memberCnt = models.IntegerField()

class OrganizationTr(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    companyStmt = models.CharField(max_length=400)

class Client(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    organization = models.ForeignKey(Organization)
    category = models.ForeignKey(Category)

# -------- end clientprofile tables --------

class Title(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

class TitleTr(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    titleName = models.CharField(max_length=50)

#no translation table is needed since client-provider will communicate via one language
class Feedback(models.Model):
    # This field is required.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Other fields here
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    languageCode = models.CharField(max_length=2)
    feedback = models.CharField(max_length=400)
    rate = models.IntegerField()

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