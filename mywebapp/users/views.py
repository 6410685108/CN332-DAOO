from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
            return redirect('/')
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
        
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'message': 'Username already exists'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'message': 'Email already exists'})
        elif password != cpassword:
            return render(request, 'users/register.html', {'message': 'Passwords do not match'})
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, 'users/signup.html')

def register(request):
    return render(request, 'users/register.html')