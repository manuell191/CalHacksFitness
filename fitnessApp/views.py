from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm, SetupForm
from .models import Profile

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    return render(request, 'home.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            messages.error(request, 'Username OR password is incorrect')
    
    context = {'form': LoginForm}
    return render(request, 'login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                messages.error(request, 'Passwords do not match')
            else:
                User.objects.create_user(username=username, password=password1)
                user = User.objects.get(username=username)
                userId = user.id
                profile = Profile(user=user)
                profile.save()

                user = authenticate(request, username=username, password=password1)
                login(request, user)
                return redirect(f'/signup/{userId}')
    context = {'form': SignupForm}
    return render(request, 'signup.html', context)
    
def setup(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = Profile.objects.get(id=pk)
    
    if user.bmi != 0:
        return redirect('home')
    
    if request.method == 'POST':
        form = SetupForm(request.POST)

        if form.is_valid():
            weight = request.POST.get('weight')
            height = request.POST.get('height')

            user.weight = weight
            user.height = height
            user.bmi = (int(weight)/(int(height)**2)) * 703
            user.goal = request.POST.get('goal')
            user.save()

            return redirect('home')
        
    context = {'form': SetupForm}
    return render(request, 'setup.html', context)

def userLogout(request):
    logout(request)
    return redirect('signup')