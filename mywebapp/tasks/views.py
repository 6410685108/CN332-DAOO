from django.shortcuts import redirect, render
from .models import Loop, Task

# Create your views here.

def loop(request):
    if request.method == "POST":
        name = request.POST['name']
        x1 = request.POST['x1']
        x2 = request.POST['x2']
        x3 = request.POST['x3']
        x4 = request.POST['x4']
        y1 = request.POST['y1']
        y2 = request.POST['y2']
        y3 = request.POST['y3']
        y4 = request.POST['y4']
        direction = request.POST['direction']
        Loop.objects.create(name=name,x1=x1,x2=x2,x3=x3,x4=x4,y1=y1,y2=y2,y3=y3,y4=y4,direction=direction).save
        
        loops = Loop.objects.all()
        return render(request, 'tasks/task.html',
                      {
                          "loops" : loops
                      }
                      )

    return render(request, 'tasks/loop.html')

def result(request):
    return render(request, 'tasks/result.html')

def task(request,name):
    thisTask = Task.objects.get(name=name)
    loops = Loop.objects.filter(task=thisTask)
    return render(request, 'tasks/task.html',
                {
                    "loops" : loops,
                }
                )

def deleteLoop(request):
    loopid = request.POST['loopid']
    Loop.objects.get(id=loopid).delete()
    return redirect('/task')

def newtask(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        Task.objects.create(name=name,address=address , owner=request.user.username).save()
        return redirect('/task')

    return render(request, 'tasks/newtask.html')

def deletetask(request):
    taskid = request.POST['taskid']
    Task.objects.get(id=taskid).delete()
    return redirect('/task')