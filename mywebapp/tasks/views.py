from django.shortcuts import render

# Create your views here.

def newtask(request):
    # newtask
    return render(request, 'tasks/newtask.html')