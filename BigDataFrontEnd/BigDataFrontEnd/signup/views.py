from .forms import SignUpForm
from django.shortcuts import render

def register(request):
    form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
