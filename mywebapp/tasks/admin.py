from django.contrib import admin
from .models import Loop

# Register your models here.
class LoopAdmin(admin.ModelAdmin):
    model = Loop
    list_display = ['name', 'date' ]

admin.site.register(Loop, LoopAdmin)