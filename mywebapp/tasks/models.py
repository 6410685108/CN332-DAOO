from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64,default="-")
    address = models.CharField(max_length=64,default="-")
    owner = models.CharField(max_length=64,default="-")
    date = models.DateField(auto_now_add=True)
    # video
    # result
    def get_all_loops(self):
        return self.loops.all()

class Loop(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=64,default="-")
    x1 = models.IntegerField(default=0)
    x2 = models.IntegerField(default=0)
    x3 = models.IntegerField(default=0)
    x4 = models.IntegerField(default=0)
    y1 = models.IntegerField(default=0)
    y2 = models.IntegerField(default=0)
    y3 = models.IntegerField(default=0)
    y4 = models.IntegerField(default=0)
    direction = models.CharField(max_length=64,default="-")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='loops',default=None)

