from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# user app
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    email2 = models.EmailField(blank=True, null=True)
    isProvider = models.BooleanField(default=False)
    isClient = models.BooleanField(default=False)

class UserProfileTr(models.Model): 
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    bioC = models.CharField(max_length=400, blank=True, null=True)
    bioP = models.CharField(max_length=400, blank=True, null=True)

class RateAgg(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    ProviderRateAgg = models.DecimalField(max_digits=3, decimal_places=2)
    ClientRateAgg = models.DecimalField(max_digits=3, decimal_places=2)


# -------- clientprofile tables (placed in user.models due to circular dependencies, can't compile otherwise) --------

class Organization(models.Model):
    memberCnt = models.IntegerField(default=1)

class OrganizationTr(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    companyStmt = models.CharField(max_length=400, blank=True, null=True)

class Client(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other fields here
    organization = models.ForeignKey(Organization, blank=True, null=True)

# -------- end clientprofile tables --------

# -------- providerprofile tables (placed in user.models due to circular dependencies, can't compile otherwise) --------
class Provider(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class SkillDef(models.Model):
    pass

class SkillDefTr(models.Model):
    skillDef = models.ForeignKey(SkillDef, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    skillName = models.CharField(max_length=50)

class Skill(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=0)
    skillDef = models.ForeignKey(SkillDef, on_delete=models.CASCADE, default=0)

#temp table. Create new standard skill name for Skill table.
class UndefinedSkill(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=0)

    languageCode = models.CharField(max_length=2)
    undefinedSkill = models.CharField(max_length=50)

# -------- end providerprofile --------

class CategoryDef(models.Model):
    pass

class CategoryDefTr(models.Model):
    categoryDef = models.ForeignKey(CategoryDef, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    categoryName = models.CharField(max_length=50)

class CategoryProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    categoryDef = models.ForeignKey(CategoryDef, on_delete=models.CASCADE)
    categoryNum = models.IntegerField(default=1)

class CategoryClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    categoryDef = models.ForeignKey(CategoryDef, on_delete=models.CASCADE)
    categoryNum = models.IntegerField(default=1)

class Title(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)

class TitleTr(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    titleName = models.CharField(max_length=50, blank=True, null=True)

class LanguageDef(models.Model):
    pass

class LanguageDefTr(models.Model):
    languageDef = models.ForeignKey(LanguageDef, on_delete=models.CASCADE)

    languageCode = models.CharField(max_length=2)
    languageName = models.CharField(max_length=50) 

class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    languageDef = models.ForeignKey(LanguageDef, on_delete=models.CASCADE, default=0)
    languageNum = models.IntegerField(default=1)

#no translation table is needed since client-provider will communicate via one language
class Feedback(models.Model):
    # The reviewer
    user = models.ForeignKey(User)

    # Other fields here
    client = models.ForeignKey(Client, blank=True, null=True)
    provider = models.ForeignKey(Provider, blank=True, null=True)
    languageCode = models.CharField(max_length=2)
    feedback = models.CharField(max_length=400, blank=True, null=True)
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