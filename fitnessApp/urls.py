from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/<pk>/', views.setup, name='setup'),
    path('logout/', views.userLogout, name='logout')
]
