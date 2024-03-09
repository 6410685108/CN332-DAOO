from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import CustomUser

# Create your views here.
def home(request):
    return render(request, 'users/index.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            message = "Invalid username or password"
    else:
        message = None
    return render(request, 'users/login.html', {'message': message})

def userLogout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'message': 'Username already exists'})
        elif CustomUser.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'message': 'Email already exists'})
        elif password != cpassword:
            return render(request, 'users/register.html', {'message': 'Passwords do not match'})
        else:
            user = CustomUser.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('/home')
    return render(request, 'users/signup.html')

def register(request):
    return render(request, 'users/register.html')

def admin(request):
    return render(request, 'users/admin.html')