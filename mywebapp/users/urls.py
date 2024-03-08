from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    
]
