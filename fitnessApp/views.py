from django.shortcuts import render
from .models import User


# Create your views here.

def userInput(request):
    if request.method == "POST":
        User.user = request.POST.get('user')
        User.height = request.POST.get('height')
        User.weight = request.POST.get('weight')
        User.bmi = (User.weight/(User.height**2)) * 703;
    User.save()

def home(request):
    return render(request, 'home.html')

def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if user is not None:
            login(request, user)
            return redirect('home.html')