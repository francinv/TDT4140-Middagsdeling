from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
@login_required
def home(request):
    return render(request, 'APP/home.html')
