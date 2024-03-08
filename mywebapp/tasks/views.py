from django.shortcuts import render

# Create your views here.

def newtask(request):
    # newtask
    return render(request, 'tasks/newtask.html')

def loop(request):
    return render(request, 'tasks/loop.html')

def result(request):
    return render(request, 'tasks/result.html')