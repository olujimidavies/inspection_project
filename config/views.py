from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Inspection, Condition

def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
    
    return render(request, 'login.html', {'error_message': error_message})

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