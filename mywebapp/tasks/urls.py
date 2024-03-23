from django.urls import path
from . import views

urlpatterns = [
    path('createtask', views.newtask, name='newtask'),
    path('loop', views.loop, name='loop'),
    path('result', views.result, name='result'),
    path('task', views.task, name='task'),
    path('deleteloop', views.deleteLoop, name='deleteloop'),
    path('newtask', views.newtask, name='newtask'),
]
