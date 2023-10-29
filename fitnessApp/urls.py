from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-input/', views.userInput, name='User-Input'),
    path('sign-in/', views.signIn, name='sign-in'),
]
