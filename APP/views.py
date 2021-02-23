from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Middag


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


class MiddagDetailView(DetailView):
    model = Middag


class MiddagCreateView(CreateView):
    model = Middag
    fields = ['title', 'content', 'guests', 'sharing', 'allergener', 'sharing_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MiddagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Middag
    fields = ['title', 'content', 'guests', 'sharing', 'allergener', 'sharing_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class MiddagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Middag
    success_url = 'home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
