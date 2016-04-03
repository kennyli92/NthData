from providerprofile.forms import ProviderEditForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user.models import UserProfile, Provider, Title, TitleTr


def provider_profile(request):

    if (request.method == 'POST') and ('providerProfileUpdate' in request.POST):
        userObj = get_object_or_404(User, id=26)   
            
        providerObj, created = Provider.objects.get_or_create(user=userObj)
  
        titleObj, created = Title.objects.get_or_create(provider=providerObj)

        titleTrObj = TitleTr.objects.create(title=titleObj, titleName=request.POST['title'])

        titleTrObj.save();

        return HttpResponseRedirect('/account/signup/success')
    else:
        form = ProviderEditForm()
        return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')



    
          
    

