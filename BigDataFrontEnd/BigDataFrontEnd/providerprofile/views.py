﻿from providerprofile.forms import ProviderEditForm
from django.shortcuts import render

def provider_profile(request):
    form = ProviderEditForm()

    return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')
    
          
    

