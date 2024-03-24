from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    task = Task.objects.all()
    return render(request, 'users/index.html',{ 'tasks': task})

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
            return render(request, 'user/signup.html',{
                'message' : 'Username already exists.'
            })
        elif CustomUser.objects.filter(email=email).exists():
            return render(request, 'user/signup.html',{
                'message' : 'Email already exists'
            })
        elif password != cpassword:
            return render(request, 'user/signup.html',{
                'message' : 'Passwords do not match'
            })
        else:
            request.session['signup_username'] = username
            request.session['signup_email'] = email
            request.session['signup_password'] = password

            return redirect('/register')
    return render(request, 'users/signup.html')
        
def register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        role = request.POST['role']
        
        username = request.session.get('signup_username')
        email = request.session.get('signup_email')
        password = request.session.get('signup_password')
       
        # try :
        user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        phone=phone,
        first_name=firstname,
        last_name=lastname,
        role=role
        )
        # except:
        #     return render(request, 'users/register.html',{
        #                 'message' : "Please upload you picture"
        #             })
        
        del request.session['signup_username']
        del request.session['signup_email']
        del request.session['signup_password']

        login(request, user)
        return redirect('/home')

    return render(request, 'users/register.html')

@login_required
def admin(request):
    user = CustomUser.objects.all()
    return render(request, 'users/admin.html', {'users': user})

def deleteUser(request):
    username = request.POST['username']
    user = CustomUser.objects.get(username=username)
    user.delete()
    return redirect('/userconfig')