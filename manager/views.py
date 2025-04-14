from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import PasswordEntry
from .forms import AddEntryForm

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'entries': entries})

@login_required
def add_view(request):
    if request.method == 'POST':
        form = AddEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = AddEntryForm()
    return render(request, 'add.html', {'form': form})

@login_required
def update_view(request, id):
    entry = get_object_or_404(PasswordEntry, id=id, user=request.user)
    if request.method == 'POST':
        form = AddEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddEntryForm(instance=entry)
    return render(request, 'update.html', {'form': form})

@login_required
def delete_view(request, id):
    entry = get_object_or_404(PasswordEntry, id=id, user=request.user)
    entry.delete()
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')

def csrf_failure(request, reason=""):
    return render(request, '403_csrf.html', {'reason': reason})
