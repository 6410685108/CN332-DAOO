from django.urls import path
from . import views

urlpatterns = [
    path('createtask', views.newtask, name='newtask'),
    
]
