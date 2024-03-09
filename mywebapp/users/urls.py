from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('userconfig/', views.admin, name='userconfig'),
    
]
