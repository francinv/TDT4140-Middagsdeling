from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'APP/index.html')

def create_post(request):
    return render(request, 'APP/create-post.html')

def base(request):
    return render(request, 'APP/base.html')
