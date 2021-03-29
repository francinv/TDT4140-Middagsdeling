from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, SendMessageForm
from .models import Message


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            messages.success(request, f'Account created for {name}!')
            return redirect('APP-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def send_message(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user
            fs.save()
            return redirect('APP-home')
    else:
        form = SendMessageForm()
    return render(request, 'users/send_message.html', {'form': form})


def user_messages(request):
    context = {
        'messages': Message.objects.filter(author=request.user) | Message.objects.filter(to_user=request.user)
    }
    return render(request, 'users/messages.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')

