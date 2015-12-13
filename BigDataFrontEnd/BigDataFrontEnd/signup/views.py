from .forms import SignUpForm
from django.shortcuts import render

def register(request):
    form = SignUpForm()

    return render(request, 'SignUpForm.html', {'form': form})
