from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Inspection, Condition

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'You have entered an invalid username or password. Please try again')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    inspections = Inspection.objects.all()
    return render(request, 'home.html', {'inspections': inspections, 'username': request.user.username})

@login_required(login_url='login')
def conditions_view(request, inspection_id):
    inspection = Inspection.objects.get(id=inspection_id)
    conditions = Condition.objects.filter(Inspection=inspection)
    return render(request, 'conditions.html', {
        'inspection': inspection, 
        'conditions': conditions,
        'username': request.user.username
    }) 