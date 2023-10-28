from django.shortcuts import render
from .models import User

# Create your views here.
#Weight / height(inches)
def calculateBMI(request):
    return User.weight/User.height * 703;

def home(request):
    return render(request, 'home.html')
