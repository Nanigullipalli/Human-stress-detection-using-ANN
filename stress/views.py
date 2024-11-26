from django.shortcuts import render
from .models import StressInput
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'stress/login.html', {'error': 'Invalid credentials'})
    return render(request, 'stress/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'stress/dashboard.html')
def collect_data(request):
    if request.method == "POST":
        data = StressInput(
            snoring_rate=request.POST['snoring_rate'],
            respiratory_rate=request.POST['respiratory_rate'],
            body_temperature=request.POST['body_temperature'],
            limb_movement=request.POST['limb_movement'],
            blood_oxygen_level=request.POST['blood_oxygen_level'],
            eye_movement=request.POST['eye_movement'],
            sleeping_hours=request.POST['sleeping_hours'],
            heart_rate=request.POST['heart_rate'],
            stress_level=request.POST['stress_level'],
        )
        data.save()
        return render(request, 'stress/success.html')
    return render(request, 'stress/collect_data.html')
def home(request):
    return render(request, 'stress/home.html')  # Render a homepage template

