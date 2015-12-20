from signup.forms import SignUpForm
from django.shortcuts import render
from django.views.generic.edit import FormView

def register(request):
    form = SignUpForm()

    return render(request, 'signup/signup.html', {'form': form})
