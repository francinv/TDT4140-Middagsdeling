from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Middag
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


@login_required
def home(request):
    context = {
        'middager': Middag.objects.all()
    }
    return render(request, 'APP/home.html', context)

class MiddagListView(ListView):
    model = Middag
    template_name = 'APP/home.html'
    context_object_name = 'middager'
    ordering = ['-date_posted']

