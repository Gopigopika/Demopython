from django.shortcuts import render,redirect
from django.contrib.auth.models import AbstractUser,User,auth
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password = request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            message.info(request,'login.html')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        username1=request.POST['uname']

        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd1']


        cpassword=request.POST['pwd2']
        if password==cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username1,email=email,password=password,first_name=firstname,last_name=lastname)
                user.save();
                return redirect('login')
                print('User created')
        else:
           messages.info(request,'Password not matched')
           return redirect('register')
        return redirect('/')
    return render(request,'register.html')