"""
Definition of urls for BigDataFrontEnd.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.contrib.auth import views as auth_views
from signup.views import signup, login

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),    
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^accounts/login/$', 
        auth_views.login, 
        {'template_name': 'signup/login.html'}),
    url(r'^account/$', 'signup.views.login', name='login'),
    url(r'^account/signup/$', 'signup.views.signup', name='signup'),
    url(r'^account/signup/success/$', 'signup.views.register_success', name='registerSuccess'),
    url(r'^account/passwordrecovery/$', 'signup.views.password_recover', name='passwordrecovery'),
    url(r'^account/passwordrecovery/emailsent/$', 'signup.views.password_recover_email_sent', name='password_recover_email_sent'),
    url(r'^account/passwordrecovery/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            'signup.views.reset_confirm', name='reset_confirm'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
