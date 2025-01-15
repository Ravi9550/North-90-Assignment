from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message

@login_required
def profile(request):
    return render(request, 'profile.html')
def registerview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the newly created user
            return redirect('singlechat')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('singlechat')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

@login_required
def singlechat(request):
    # all_users = everyone except the logged-in user
    all_users = User.objects.exclude(id=request.user.id)
    return render(request, 'singlechat.html', {'all_users': all_users})

@login_required
def get_old_messages(request, username):
    """Return JSON list of past messages between request.user and 'username'."""
    try:
        other_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse([], safe=False)

    msgs = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    data = []
    for m in msgs:
        data.append({
            'sender': m.sender.username,
            'content': m.content,
            'timestamp': m.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })

    return JsonResponse(data, safe=False)